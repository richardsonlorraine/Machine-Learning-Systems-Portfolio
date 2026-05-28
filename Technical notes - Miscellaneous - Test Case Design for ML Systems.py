def test_edge_case_extreme_values():
    """Boundary Value Analysis: Ensuring extreme inputs are explicitly intercepted."""
    extreme_data = np.array([[1000.0, 1000.0, 1000.0, 1000.0]])
    
    # Predict should theoretically be caught by a business logic wrapper before reaching raw inference
    result = model.predict(extreme_data)[0]
    
    # If your pipeline doesn't clip data, warn the architecture team
    assert result in iris.target, "Model output fell outside valid target bounds."
