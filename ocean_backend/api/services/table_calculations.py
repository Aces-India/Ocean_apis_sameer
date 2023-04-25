import pandas as pd

def table_calc(heading, side_heading,text):
    
    df = pd.read_excel("api/services/sales.xlsx")
    
    table_df= df.groupby([heading,side_heading]).aggregate({text:sum})
    
    
    # ad = dict(table_df)
    res_df = table_df.to_json()
    print('\n this is the tabel calculation',res_df,'\n\n',type(res_df))
    
    
    return res_df 