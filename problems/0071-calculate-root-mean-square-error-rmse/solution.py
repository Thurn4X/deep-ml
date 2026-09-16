import numpy as np
def rmse(y_true, y_pred):
	# Write your code here
	if y_true is None or y_pred is None or len(y_true) != len(y_pred):
		return None
	else:
		y_true = np.array(y_true)
		y_pred = np.array(y_pred)
		erreur_quadratique_moyenne = np.mean((y_true - y_pred)**2)
		rmse_res = np.sqrt(erreur_quadratique_moyenne)
		return round(rmse_res,3)
