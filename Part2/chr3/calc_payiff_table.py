import numpy as np
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

def calc_payoff_table(fixed_cost, run_cost, sale_price,
                        machine_ability, demand_boom, demand_slump):
                        
    # 出荷された製品の個数
    num_product_df = pd.DataFrame({
        '0台': [0, 0],
        '1台': [min([machine_ability, demand_boom]),
            min(machine_ability, demand_slump)],
        '2台': [min([machine_ability * 2, demand_boom]),
            min(machine_ability * 2, demand_slump)],
    })
    
    # 売り上げ行列
    sales_df = num_product_df * sale_price

    # 製造コスト
    run_cost_df = pd.DataFrame({
        '0台': np.repeat(fixed_cost, 2),
        '1台': np.repeat(fixed_cost + run_cost, 2),
        '2台': np.repeat(fixed_cost + run_cost * 2, 2)
    })

    #　利得行列
    payoff_df = sales_df - run_cost_df
    payoff_df.index = ['好調', '不調']

    #　結果を返す
    return payoff_df