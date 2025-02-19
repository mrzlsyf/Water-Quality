# 🫗 Water Quality 🚿
🚀 This project leverages machine learning to classify drinking water quality based on various physicochemical properties.

---

## 🎯 Overview
This system performs the following key tasks:
1. **Data Preprocessing & Feature Engineering** 🛠️
2. **Exploratory Data Analysis (EDA) for Water Quality Insights** 📊
3. **Machine Learning Model Implementation for Water Classification** 🤖
4. **Model Deployment using Streamlit** 🚀

This predictive model helps in determining whether water is safe for consumption or not based on specific chemical compositions.

---

## 📂 Dataset
The dataset used in this project is **water_potability.csv**, which consists of several physicochemical parameters of water, such as:
- **pH**
- **Hardness**
- **Solids**
- **Chloramines**
- **Sulfate**
- **Conductivity**
- **Organic Carbon**
- **Trihalomethanes**
- **Turbidity**
- **Potability** (Target variable: 0 = Not Potable, 1 = Potable)

---

## 🏠 Project Workflow 📌
1. **Data Collection & Cleaning** 🧹
   - Load dataset and handle missing values.
   - Perform feature selection and scaling.
2. **Exploratory Data Analysis (EDA)** 🔍
   - Visualize water quality distribution.
   - Identify key factors affecting potability.
3. **Model Training & Evaluation** 🏗️
   - Train a **Random Forest Classifier** for water classification.
   - Evaluate model performance using accuracy, precision, recall, and F1-score.
4. **Model Deployment using Streamlit** 🌍
   - Build an interactive web application for real-time water quality prediction.

---

## 📂 Project Structure 🛠️
```
📚 Water-Quality/
├── 📙 Code Model.ipynb             # Jupyter Notebook for model training and analysis
├── 📘 streamlit_water_quality.py   # Streamlit app for real-time water classification
├── 📗 water_potability.csv         # Dataset containing water quality parameters
├── ⚖️ model.pkl                    # Trained Random Forest model
├── 📖 requirements.txt             # List of dependencies
```

---

## ✨ Features
✅ **Classifies drinking water quality based on physicochemical properties**  

✅ **Implements Random Forest for robust classification**  

✅ **Provides interactive prediction using a Streamlit web app**  

✅ **Explores key water quality factors through EDA**  

---

## 🛠 Technologies & Libraries
🔹 **Python** 🐍  

🔹 **Pandas & NumPy** 📊  

🔹 **Scikit-Learn** 🤖  

🔹 **Matplotlib & Seaborn** 🎨  

🔹 **Streamlit** 🌍  

---

## 🚀 Installation

Ensure you have Python installed, then install dependencies:
```sh
pip install -r requirements.txt
```

---
## 🎥 Usage
Run the Jupyter Notebook for data analysis and model training:
```sh
jupyter notebook "Code Model.ipynb"
```
To launch the Streamlit web app for real-time predictions:
```sh
streamlit run streamlit_water_quality.py
```

---

## 📊 Results
- **Identifies key factors affecting drinking water quality.**
- **Provides an accurate classification model using Random Forest.**
- **Deploys an interactive web application for public use.**

---

## 🌟 Future Improvements
🌟 Implement **Deep Learning models** for improved accuracy.  

🌟 Extend dataset with **real-time water quality data sources**.  

🌟 Enhance Streamlit app with **more visualizations and explanations**.  

---

## 🌍 Contributing
Contributions are welcome! Follow these steps to contribute:
1. **Fork the repository** 🌿  
2. **Create a new branch** 🌱  
3. **Make your changes** ✨  
4. **Submit a pull request** 🛠

*If you find this project useful, please **star ⭐ the repository** and share it with others!*  

---

>  **🏰 Clean water is a basic human right. Predicting its quality helps ensure safer communities. 🚀🌟**
