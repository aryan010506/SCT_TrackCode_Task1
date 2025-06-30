import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression

# Step 1 — Load training data
data = pd.read_csv(r"C:\Users\Aryan\OneDrive\Desktop\machine learning\train.csv")

# Keep only required features
X = data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = data['SalePrice']

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 2 — Create the GUI
def predict_price():
    try:
        sqft = float(entry_sqft.get())
        bedrooms = int(entry_bedrooms.get())
        baths = int(entry_baths.get())
        
        # Create input dataframe
        input_data = pd.DataFrame([[sqft, bedrooms, baths]], columns=['GrLivArea', 'BedroomAbvGr', 'FullBath'])
        
        # Predict
        price = model.predict(input_data)[0]
        
        messagebox.showinfo("Prediction", f"Estimated House Price: ₹ {int(price):,}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# Create window
window = tk.Tk()
window.title("House Price Predictor")

# Add labels and entry fields
tk.Label(window, text="Square Footage (GrLivArea):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_sqft = tk.Entry(window)
entry_sqft.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Number of Bedrooms:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_bedrooms = tk.Entry(window)
entry_bedrooms.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Number of Bathrooms:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_baths = tk.Entry(window)
entry_baths.grid(row=2, column=1, padx=10, pady=5)

# Predict Button
predict_button = tk.Button(window, text="Predict Price", command=predict_price)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
