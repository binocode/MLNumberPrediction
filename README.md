# Random Forest Regression Example

This repository contains a Python script demonstrating the use of a Random Forest Regressor for predicting numeric values based on input data. The script includes data loading from a JSON file, data preprocessing, model training, evaluation, and visualization.

## Requirements

Make sure you have the following libraries installed:

- `numpy`
- `scikit-learn`
- `matplotlib`
- `json`

You can install these dependencies using the following command:

```bash
pip install numpy scikit-learn matplotlib
```
Usage

1. Clone the repository:

```bash
git clone https://github.com/binocode/MLNumberPrediction.git
cd MLNumberPrediction
```

2. Run the script:

```bash
python main.py
```

3. Examine the output, including the Mean Squared Error (MSE) and visualizations of actual vs. predicted values.

Customization

Feel free to modify the script to suit your specific use case:

    Adjust the number of estimators in the Random Forest Regressor (n_estimators parameter).
    Change the input data or use your own dataset in JSON format.
    Explore different evaluation metrics or add additional visualizations.
    Change the DEVELOPMENT to `True` if you want to see the matplotlib representation

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    The script uses the scikit-learn library for machine learning.

If you find this code useful or have suggestions for improvement, please feel free to contribute or open an issue.