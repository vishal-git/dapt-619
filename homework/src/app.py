"""Part 4: a churn prediction app for the retention team. Run from the repo root:  python src/app.py"""
import gradio as gr
import joblib
import polars as pl

bundle = joblib.load("models/churn_model.joblib")  # saved by src/train.py
model, columns = bundle["model"], bundle["columns"]

TEXT_COLUMNS = ["gender", "contract_type", "payment_method", "paperless_billing", "internet_service",
                "phone_service", "online_security", "tech_support"]


def predict(age, tenure, monthly, contract, payment, internet, security, support, paperless, gender, phone):
    # step 1: if monthly is not positive, stop with a clear message: raise gr.Error("...")
    # --

    no_internet = internet == "No"
    row = pl.DataFrame({
        "age": [age], "tenure_months": [tenure], "monthly_charges": [monthly], "total_charges": [tenure * monthly],
        "gender": [gender], "contract_type": [contract], "payment_method": [payment], "paperless_billing": [paperless],
        "internet_service": [internet], "phone_service": [phone],
        "online_security": ["No internet service" if no_internet else security],
        "tech_support": ["No internet service" if no_internet else support],
    })
    # one row only has one category per column, so add the dummy columns it's missing (as 0)
    # and put them in the same order the model was trained on
    X = row.to_dummies(columns=TEXT_COLUMNS).to_pandas().reindex(columns=columns, fill_value=0).astype(float)
    return f"Churn probability: {model.predict_proba(X)[0, 1]:.0%}"


inputs = [
    gr.Slider(18, 90, value=35, step=1, label="Age"),
    gr.Slider(0, 72, value=6, step=1, label="Tenure (months)"),
    gr.Number(value=85, label="Monthly charges ($)"),
    gr.Dropdown(["Month-to-month", "One year", "Two year"], value="Month-to-month", label="Contract"),
    gr.Dropdown(["Electronic check", "Mailed check", "Bank transfer", "Credit card"], value="Electronic check", label="Payment method"),
    gr.Dropdown(["DSL", "Fiber optic", "No"], value="Fiber optic", label="Internet service"),
    gr.Radio(["Yes", "No"], value="No", label="Online security"),
    gr.Radio(["Yes", "No"], value="No", label="Tech support"),
    gr.Radio(["Yes", "No"], value="Yes", label="Paperless billing"),
    gr.Radio(["Male", "Female"], value="Female", label="Gender"),
    gr.Radio(["Yes", "No"], value="Yes", label="Phone service"),
]

# step 2: create a gr.Interface with fn=predict, inputs=inputs, outputs="text", and a title
# --

if __name__ == "__main__":
    # step 3: launch the app
    # --
    pass  # replace this line with your code
