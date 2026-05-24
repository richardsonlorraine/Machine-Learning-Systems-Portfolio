import ipytest
import pytest
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier # --- Operational Setup ---
ipytest.autoconfig()
iris = load_iris()
X, y = iris.data, iris.target
model = DecisionTreeClassifier().fit(X, y) # --- Test Suite ---
def test_typical_case():
    """Requirement: Accurate classification of standard domain data."""
    input_data = np.array([[4.5, 2.3, 1.3, 0.3]])
    expected_output = 0 # Setosa
    result = model.predict(input_data)[0]
    assert result == expected_output
def test_edge_case_extreme_values():
    """Boundary Analysis: System should handle outliers without crashing."""
    extreme_data = np.array([[1000, 1000, 1000, 1000]])
    try:        # We test if the model can still produce an output (robustness)
        result = model.predict(extreme_data)    
        assert result is not None  
    except Exception as e:
        pytest.fail(f"Model crashed on extreme boundary: {e}")
def test_error_handling_missing_values():
    """Error Injection: Pipeline must trigger ValueError for nulls."""
    input_data = np.array([[None, None, None, None]])
    with pytest.raises(ValueError):
        model.predict(input_data) # Execute Automated Tests
ipytest.run('-v')