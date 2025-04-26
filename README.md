
# Plant Disease Classification using CNN

![Project Banner](path/to/your/banner_image.png) <!-- Add your banner image here -->

A deep learning project that classifies plant diseases using Convolutional Neural Networks (CNN). This model can distinguish between healthy plants and those affected by powdery mildew (oïdium) or rust (rouille).

## Key Features
- 🖼️ Image preprocessing and data augmentation
- 🧠 Custom CNN architecture with 92% test accuracy
- 📊 Training visualization and model evaluation
- 🚀 Ready-to-use prediction system

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Training the Model](#training-the-model)
- [Results](#results)
- [Roadmap](#roadmap)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plant-disease-classification.git
   cd plant-disease-classification
   ```

2. Install dependencies:
   ```bash
   pip install tensorflow matplotlib numpy pillow
   ```

## Dataset

The dataset contains images of plants in three categories:
- Healthy
- Powdery Mildew (Oïdium)
- Rust (Rouille)
![image](https://github.com/user-attachments/assets/9ddfce43-b6c3-4385-85a7-77598842170e)

Dataset structure:
```
plant data/
├── Train/
│   ├── healthy/
│   ├── oidium/
│   └── rust/
├── Test/
│   ├── ...
└── Validation/
    ├── ...
```

## Training the Model

The CNN architecture consists of:
- 4 Convolutional layers with MaxPooling
- 512-neuron Dense layer with Dropout
- 3-neuron output layer (softmax)

To train the model:
```python
python src/train.py --epochs 20 --batch_size 32
```

## Results

### Model Performance
- Test Accuracy: 92%
- Training Accuracy: 94%
- Validation Accuracy: 93%

### Training Curves
![image](https://github.com/user-attachments/assets/d2206b17-f58a-42e8-9f0c-7eb49eda2b8d)


### Prediction Example
![image](https://github.com/user-attachments/assets/b09f7977-469b-41e6-bc39-5705959702be)


## Roadmap

![image](https://github.com/user-attachments/assets/4abfbc47-619c-44d0-96f3-ab14d389136d)

1. Data Collection and Preprocessing- Kaggle
2. Model Architecture Design
3. Training and Validation
4. Performance Evaluation
5. Web Application Development
6. Deployment


---

**Contributors**: Imane BENZEGUNINE & Anas HANNOUR
**Contact**: https://www.linkedin.com/in/imane-benzegunine/ and https://www.linkedin.com/in/anas-hannour/
```

### Notes for Customization:
1. Replace placeholder paths with your actual image paths
2. Add your banner/logo image at the top
3. Include your roadmap visualization image
4. Update contact information and contributor details
5. Add any additional sections specific to your project

For the roadmap image, you can create a simple diagram showing your development process using tools like:
- [Miro](https://miro.com/)
- [Lucidchart](https://www.lucidchart.com/)
- [Excalidraw](https://excalidraw.com/)
- Or even a simple PowerPoint/Google Slides timeline

Would you like me to suggest any specific improvements to the technical content or structure?
