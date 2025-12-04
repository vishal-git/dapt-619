import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
import os

from utils import CIFAR10_CLASSES

if __name__ == "__main__":
    model = nn.Sequential(
        nn.Conv2d(3, 32, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2, 2),
        nn.Conv2d(32, 64, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2, 2),
        nn.Flatten(),
        nn.Linear(64 * 8 * 8, 10)
    )

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    train_data = torchvision.datasets.CIFAR10(
        root='./data', train=True, download=True, transform=transform
    )
    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

    test_data = torchvision.datasets.CIFAR10(
        root='./data', train=False, download=True, transform=transform
    )
    test_loader = DataLoader(test_data, batch_size=64, shuffle=False)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    loss_function = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    num_epochs = 10

    for epoch in range(num_epochs):
        model.train()
        total_correct = 0
        total_samples = 0
        
        for images, labels in train_loader:
            images = images.to(device)
            labels = labels.to(device)
            
            optimizer.zero_grad()
            predictions = model(images)
            loss = loss_function(predictions, labels)
            loss.backward()
            optimizer.step()
            
            _, predicted = torch.max(predictions, 1)
            total_samples += labels.size(0)
            total_correct += (predicted == labels).sum().item()
        
        train_accuracy = 100 * total_correct / total_samples
        
        model.eval()
        test_correct = 0
        test_samples = 0
        
        with torch.no_grad():
            for images, labels in test_loader:
                images = images.to(device)
                labels = labels.to(device)
                
                predictions = model(images)
                _, predicted = torch.max(predictions, 1)
                
                test_samples += labels.size(0)
                test_correct += (predicted == labels).sum().item()
        
        test_accuracy = 100 * test_correct / test_samples
        print(f"Epoch {epoch+1}/{num_epochs} - Train: {train_accuracy:.2f}% - Test: {test_accuracy:.2f}%")

    os.makedirs('models', exist_ok=True)

    model_path = 'models/cifar10_model.pth'
    torch.save({
        'model_state_dict': model.state_dict(),
        'class_names': CIFAR10_CLASSES
    }, model_path)

    print(f"Model saved to {model_path}")
    print(f"Final test accuracy: {test_accuracy:.2f}%")
