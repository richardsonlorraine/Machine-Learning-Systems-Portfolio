from lime.lime_text import LimeTextExplainer # 1. Define the explainer
explainer = LimeTextExplainer(class_names=['Negative', 'Positive']) # 2. Choose a specific instance (a product review)
text_instance = "The service was great, but the food was quite cold." # 3. Explain the prediction
exp = explainer.explain_instance(text_instance, model.predict_proba, num_features=6) # This would output a list of words and their contribution to the score: # 'great': +0.45 (Positive) # 'cold': -0.30 (Negative)
print(exp.as_list())