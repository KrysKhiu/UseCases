import importlib
from importlib import *
from config.config_variables import *
from Lib import *



def main():
    """
    This is our main program.
    """
    
    df_join_freq_sev = MergeFreqSevTable().merge_freq_sev()

    df_join_freq_sev = PrepareTheFeatures().encoding_columns(df_join_freq_sev)

    df_join_freq_sev = PrepareTheFeatures().normalize_columns(df_join_freq_sev)

    df_join_freq_sev['RiskProbability'] = RiskToFileAClaim().predict_with_gradient_boosting(df_join_freq_sev)
    
    df_join_freq_sev['ForecastClaimAmountPerYear'] = EstimationClaimAmountOnExposure().predict_claim_amount_on_exposure(df_join_freq_sev)
    
    return df_join_freq_sev

if __name__ == '__main__':

    main()