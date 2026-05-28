from scipy.stats import ks_2samp

def detect_drift(train, production, alpha=0.05):
    """Evaluates non-parametric distribution changes between baseline and production telemetry."""
    # Returns test statistic and p-value
    _, p_value = ks_2samp(train, production)
    
    # If p-value is lower than significance level (alpha), reject null hypothesis (Drift Detected)
    return p_value < alpha
