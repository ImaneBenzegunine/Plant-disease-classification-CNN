
# Plant Disease Classification using CNN

A deep learning project that classifies plant diseases using Convolutional Neural Networks (CNN). This model can distinguish between healthy plants and those affected by powdery mildew (oïdium) or rust (rouille).


## Installation

1. Clone the repository:
   ```bash
   https://github.com/ImaneBenzegunine/Plant-disease-classification-CNN
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
![image](https://github.com/user-attachments/assets/87c3a9fa-fbaf-425f-9c07-bd8d102a39a7)


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
