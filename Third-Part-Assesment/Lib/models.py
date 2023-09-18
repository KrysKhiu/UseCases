from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import PoissonRegressor

#os.chdir('C:\\Users\\cchieu\\OneDrive - EDENRED\\Documents\\Python Experiments\\Use_Cases\\Claim_Liability_Assessment')

class EstimationClaimAmountOnExposure:
    def __init__(self):
        self
    
    def predict_claim_amount_on_exposure(self, df_join_freq_sev):
         X = df_join_freq_sev.drop(columns=['ClaimNb', 'ClaimAmountOnExposure', 'Density', 'VehGas', 'IDpol', 'FlagClaim', 'Exposure', 'ClaimAmount'])

        # select dependent variables
        y = df_join_freq_sev.loc[:, 'ClaimAmountOnExposure']
        
        model_poisson_regressor_sklearn = PoissonRegressor()
        
        return model_poisson_regressor_sklearn
        
class RiskToFileAClaim:
    def __init__(self):
        self
     
    def predict_with_gradient_boosting(self, df_join_freq_sev):
        X = df_join_freq_sev.drop(columns=['ClaimNb', 'ClaimAmountOnExposure', 'Density', 'VehGas', 'IDpol', 'FlagClaim', 'Exposure', 'ClaimAmount'])

        # select dependent variables
        y = df_join_freq_sev.loc[:, 'FlagClaim']
        
        model_gradient_boosting_sklearn = GradientBoostingClassifier()
        risk_calculation = cross_val_predict(model_gradient_boosting_sklearn, X, y, cv=3, method = 'predict_proba')
        
        return risk_calculation