import pandas as pd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def cubic(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def exp(x, a, b, c):
    return a * np.exp(b * x) + c

def log(x, a, b, c):
    # Handles zero or negative values by shifting x
    x_shifted = x + 1 - np.min(x)
    return a * np.log(b * x_shifted) + c

def format_equation(model_name, params):
    # Extended to include exp and log models
    if model_name == 'linear':
        return f'{params[0]:.2g}*x + {params[1]:.2g}'
    elif model_name == 'quadratic':
        return f'{params[0]:.2g}*x**2 + {params[1]:.3f}*x + {params[2]:.2g}'
    elif model_name == 'cubic':
        return f'{params[0]:.2g}*x**3 + {params[1]:.2g}*x**2 + {params[2]:.2g}*x + {params[3]:.3f}'
    elif model_name == 'exp':
        return f'{params[0]:.2g}*exp({params[1]:.3f}*x) + {params[2]:.3f}'
    elif model_name == 'log':
        return f'{params[0]:.3f}*log({params[1]:.3f}*x) + {params[2]:.3f}'
    else:
        return 'Complex Model'

def analyze_relationship(df):
    if df.shape[1] != 2:
        return "DataFrame must have exactly two columns"

        # Extracting the two columns as x and y
    x, y = df.iloc[:, 0], df.iloc[:, 1]

    # Ensure x and y are numeric
    if not (np.issubdtype(x.dtype, np.number) and np.issubdtype(y.dtype, np.number)):
        return "Columns must be numeric"

    model_functions = {
        'linear': linear,
        'quadratic': quadratic,
        'cubic': cubic,
        'exp': exp,
        'log': log
    }

    best_fit = None
    best_error = float('inf')

    for model_name, model_func in model_functions.items():
        try:
            params, _ = optimize.curve_fit(model_func, x, y)
            predictions = model_func(x, *params)
            error = np.mean((y - predictions) ** 2)

            if error < best_error:
                best_fit = (model_name, params)
                best_error = error
        except Exception as e:
            print(f"Error fitting model {model_name}: {e}")

    if best_fit:
        plt.scatter(x, y)
        plt.plot(x, model_functions[best_fit[0]](x, *best_fit[1]), color='red')
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        plt.title(f'Best fit: {best_fit[0]}')
        plt.show()
        equation = format_equation(best_fit[0], best_fit[1])
        print(best_fit)
        return f'Best fit equation: {equation}'
    else:
        return 'No suitable model found.'

# Example usage
# df1 = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#                     'other_col': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']})
# df2 = pd.DataFrame({'col2': [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331
