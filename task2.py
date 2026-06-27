# ==========================================================
# DecodeLabs AI Internship - Project 2
# AI Data Classification using Machine Learning
# Developed by: Kshama Jain
# ==========================================================

print("=" * 60)
print("🤖 DecodeLabs AI Internship")
print("📊 Project 2 - Iris Flower Classification")
print("=" * 60)

# Import Libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

print("\n📥 Loading Iris Dataset...")

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

print("✅ Dataset Loaded Successfully!")
print(f"📌 Total Samples : {len(X)}")
print(f"📌 Total Features : {len(iris.feature_names)}")
print(f"📌 Target Classes : {list(iris.target_names)}")

print("\n🔀 Splitting Dataset into Training and Testing Data...")

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("✅ Split Completed!")
print(f"Training Data : {len(X_train)}")
print(f"Testing Data  : {len(X_test)}")

print("\n🧠 Training Decision Tree Model...")

# Create Model
model = DecisionTreeClassifier(random_state=42)

# Train
model.fit(X_train, y_train)

print("✅ Model Trained Successfully!")

print("\n🔍 Testing the Model...")

# Predict
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\n🎯 Model Accuracy : {accuracy*100:.2f}%")

print("\n📄 Classification Report")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

print("=" * 60)
print("🌸 Predict Your Own Flower")
print("=" * 60)

try:
    sepal_length = float(input("Enter Sepal Length (cm): "))
    sepal_width = float(input("Enter Sepal Width (cm): "))
    petal_length = float(input("Enter Petal Length (cm): "))
    petal_width = float(input("Enter Petal Width (cm): "))

    sample = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    result = model.predict(sample)

    print("\n🌼 Predicted Flower Species:", iris.target_names[result][0])

except ValueError:
    print("\n❌ Please enter only numeric values.")

print("\n🎉 Project Completed Successfully!")
print("Thank you for using the Iris Flower Classifier.")