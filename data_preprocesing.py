import pandas as pd
import re
import ast # cia biblioteka, kuri padeda tvarkytis su sarasais
import os




txt_list = os.listdir('D:/data_sandbox/output')
                  
for i in txt_list:
    file_df = pd.DataFrame(columns=['Įmonės kodas',
                                'PVM mokėtojo kodas',
                                'Pardavimo pajamos',
                                'Grynasis pelnas',
                                'Vidutinis atlyginimas',
                                'Atlyginimų mediana'])

    with open(f'D:/data_sandbox/output/{i}','r', encoding='utf-8') as data_file:
        print(i)
        for row in data_file:
            print(str(row))
            for fraze in file_df.columns:
                if fraze in row:
                    if fraze == 'Įmonės kodas':
                        file_df['Įmonės kodas'] = re.findall(r'\d+', row)
                    if fraze == 'PVM mokėtojo kodas':
                        file_df['PVM mokėtojo kodas'] = 'LT' + str(re.findall(r'\d+', row)[0])
                    if fraze == 'Pardavimo pajamos':
                        try:
                            file_df['Pardavimo pajamos'] = ''.join(ast.literal_eval(str(re.findall(r'\d+', row)[1:])))
                        except:
                            file_df['Pardavimo pajamos'] = ''
                    if fraze == 'Grynasis pelnas':
                        try:
                            file_df['Grynasis pelnas'] = ''.join(ast.literal_eval(str(re.findall(r'\d+', row)[1:])))
                        except:
                            file_df['Grynasis pelnas'] = ''
                    if fraze == 'Vidutinis atlyginimas':
                        try:
                            file_df['Vidutinis atlyginimas'] = re.search(r'Vidutinis atlyginimas (.*?) €', row).group(1)
                        except:
                            file_df['Vidutinis atlyginimas'] = ''
                    if fraze == 'Atlyginimų mediana':
                        try:
                            file_df['Atlyginimų mediana'] = re.search(r'Atlyginimų mediana — (.*?) €', row).group(1) 
                        except:
                            file_df['Atlyginimų mediana'] = ''
                    if fraze == 'Pardavimo pajamos':
                        try:
                            file_df['Pardavimo pajamos'] = re.search(r'Pardavimo pajamos 2022: (.*?) €', row).group(1).replace(' ','')
                        except:
                            file_df['Pardavimo pajamos'] = ''
                    else:
                        pass
                else:
                    pass
                    # print(f'nera tokios frazes:{fraze}')

        data_file.close()
    file_df.to_excel(f'D:/data_sandbox/xlsx_data/{i[:-4]}.xlsx')


print('pasibaige failo skaitymas')




