import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

from yanyan_GetCheater import get_cheater
def judgment_cheater(name):
    model = joblib.load('models/Cheater.pkl')

    columns_ = ['karma', 'networkExp', 'bedwars_beds', 'bedwars_bedwars_challenger', 'bedwars_bedwars_killer', 'bedwars_collectors_edition', 'bedwars_level', 'bedwars_loot_box', 'bedwars_slumber_ticket_master', 'bedwars_wins', 'challenges', 'all_timeBEDWARS__defensive', 'BEDWARS__offensive', 'BEDWARS__support', 'Bedwars_openedChests', 'Experience', '_items_purchased_bedwars', 'beds_broken_bedwars', 'beds_lost_bedwars', 'coins', 'deaths_bedwars', 'diamond_resources_collected_bedwars', 'emerald_resources_collected_bedwars', 'fall_deaths_bedwars', 'fall_final_deaths_bedwars', 'fall_final_kills_bedwars', 'fall_kills_bedwars', 'final_deaths_bedwars', 'final_kills_bedwars', 'games_played_bedwars', 'games_played_bedwars_1', 'kills_bedwars', 'losses_bedwars', 'void_deaths_bedwars', 'void_final_deaths_bedwars', 'void_final_kills_bedwars', 'void_kills_bedwars', 'wins_bedwars','fkdr','wlr','bblr','fk_lev','bb_lev','kill_lev']
    # data = [[76995.0,987634.0,64.0,0.0,177.0,38.0,7.0,5.0,0.0,21.0,0.0,0.0,17.0,8.0,11.0,25853.0,2343.0,63.0,96.0,22412.0,400.0,295.0,219.0,5.0,2.0,2.0,4.0,106.0,91.0,153.0,154.0,246.0,125.0,195.0,14.0,31.0,102.0,21.0,0,0.8584905660377359,0.168,0.65625,13.0,35.142857142857146,9.0]]
    data = get_cheater(False, name)
    # data = [
        # [735.0,436149.0,110.0,0.0,320.0,64.0,13.0,1.0,0.0,31.0,0.0,0.0,22.0,21.0,0.0,56096.0,3683.0,110.0,189.0,36930.0,758.0,652.0,1022.0,9.0,3.0,1.0,13.0,187.0,164.0,219.0,219.0,534.0,183.0,362.0,80.0,47.0,255.0,31.0,0.8770053475935828,0.16939890710382513,0.582010582010582,12.615384615384615,41.07692307692308,8.461538461538462],
        # [0.0,30868.0,26.0,0.0,68.0,8.0,2.0,0.0,0.0,6.0,0.0,0.0,7.0,1.0,0.0,1925.0,249.0,26.0,3.0,612.0,9.0,41.0,4.0,0.0,0.0,1.0,3.0,1.0,68.0,7.0,7.0,40.0,1.0,6.0,0.0,5.0,9.0,6.0,68.0,6.0,8.666666666666666,34.0,20.0,13.0],
        # [5.0,74995.0,20.0,0.0,54.0,53.0,6.0,0.0,0.0,12.0,0.0,0.0,5.0,7.0,0.0,14028.0,1088.0,20.0,46.0,8998.0,134.0,219.0,81.0,4.0,0.0,2.0,2.0,50.0,49.0,59.0,59.0,122.0,47.0,84.0,18.0,8.0,24.0,12.0,0,0.98,0.2553191489361702,0.43478260869565216,8.166666666666666,20.333333333333332,3.3333333333333335],
        # [115885.0,1141497.0,271.0,0.0,580.0,265.0,15.0,14.0,0.0,36.0,0.0,0.0,64.0,47.0,35.0,64090.0,7843.0,271.0,360.0,12756.0,1151.0,1416.0,645.0,25.0,3.0,5.0,19.0,362.0,305.0,427.0,443.0,871.0,376.0,570.0,129.0,99.0,369.0,36.0,0,0.8425414364640884,0.09574468085106383,0.7527777777777778,20.333333333333332,58.06666666666667,18.066666666666666],
        # [43275.0,686458.0,108.0,1.0,273.0,168.0,12.0,4.0,0.0,83.0,0.0,0.0,27.0,12.0,12.0,47918.0,4252.0,108.0,39.0,81410.0,503.0,322.0,96.0,22.0,2.0,6.0,28.0,34.0,273.0,114.0,114.0,325.0,31.0,249.0,15.0,92.0,153.0,83.0,0,8.029411764705882,2.6774193548387095,2.769230769230769,22.75,27.083333333333332,9.0],
        # [36410.0,632665.0,257.0,0.0,539.0,148.0,11.0,15.0,0.0,48.0,0.0,0.0,63.0,40.0,42.0,45204.0,7118.0,255.0,150.0,19216.0,596.0,1234.0,663.0,19.0,5.0,6.0,15.0,175.0,355.0,226.0,235.0,539.0,177.0,320.0,53.0,119.0,207.0,48.0,0,2.0285714285714285,0.2711864406779661,1.7,32.27272727272727,49.0,23.181818181818183],
        # [490.0,414719.0,68.0,0.0,450.0,1044.0,20.0,19.0,0.0,105.0,0.0,0.0,8.0,31.0,48.0,89538.0,6111.0,68.0,408.0,14195.0,2232.0,1082.0,555.0,50.0,11.0,10.0,26.0,419.0,242.0,540.0,594.0,1030.0,435.0,1364.0,169.0,66.0,393.0,105.0,0,0.5775656324582339,0.2413793103448276,0.16666666666666666,12.1,51.5,3.4],
        # [5.0,121678.0,22.0,0.0,68.0,20.0,4.0,3.0,0.0,5.0,0.0,0.0,5.0,3.0,9.0,6419.0,841.0,22.0,20.0,7647.0,93.0,143.0,47.0,0.0,0.0,0.0,1.0,23.0,36.0,30.0,30.0,106.0,24.0,56.0,7.0,14.0,39.0,5.0,0,1.565217391304348,0.20833333333333334,1.1,9.0,26.5,5.5],
        # [10.0,146812.0,48.0,0.0,100.0,21.0,5.0,0.0,0.0,22.0,0.0,0.0,14.0,7.0,0.0,12835.0,1191.0,48.0,32.0,18571.0,108.0,144.0,69.0,2.0,1.0,3.0,7.0,28.0,93.0,54.0,54.0,141.0,32.0,49.0,8.0,15.0,50.0,22.0,0,3.3214285714285716,0.6875,1.5,18.6,28.2,9.6],
        # [36940.0,1080679.0,50.0,0.0,150.0,17.0,5.0,0.0,0.0,14.0,0.0,0.0,12.0,7.0,0.0,15358.0,1493.0,50.0,72.0,6230.0,177.0,256.0,52.0,3.0,0.0,5.0,3.0,69.0,107.0,85.0,89.0,159.0,69.0,75.0,19.0,23.0,57.0,14.0,0,1.5507246376811594,0.2028985507246377,0.6944444444444444,21.4,31.8,10.0],
        # [2050135.0,32785528.0,1556.0,30.0,4746.0,6382.0,143.0,165.0,0.0,680.0,0.0,0.0,209.0,260.0,476.0,691986.0,49102.0,1523.0,876.0,942793.0,4459.0,13434.0,7344.0,100.0,21.0,50.0,124.0,752.0,2759.0,1431.0,1643.0,4683.0,721.0,2587.0,326.0,774.0,1736.0,673.0,1,3.668882978723404,0.9334257975034674,1.7385844748858448,19.293706293706293,32.74825174825175,10.65034965034965],
        # [19917800.0,90112043.0,366.0,0.0,494.0,488.0,33.0,80.0,0.0,94.0,0.0,0.0,19.0,21.0,214.0,154955.0,5632.0,362.0,260.0,368950.0,876.0,2406.0,1863.0,23.0,5.0,8.0,18.0,229.0,377.0,320.0,341.0,859.0,233.0,372.0,91.0,151.0,409.0,87.0,1,1.6462882096069869,0.37339055793991416,1.3923076923076922,11.424242424242424,26.03030303030303,10.969696969696969],
        # [10474095.0,37487604.0,352.0,0.0,1156.0,869.0,37.0,56.0,0.0,209.0,0.0,0.0,58.0,32.0,150.0,176035.0,11219.0,328.0,278.0,438369.0,1525.0,1746.0,1271.0,37.0,6.0,11.0,54.0,254.0,699.0,462.0,551.0,1747.0,266.0,850.0,99.0,238.0,811.0,196.0,1,2.751968503937008,0.7368421052631579,1.1798561151079137,18.89189189189189,47.21621621621622,8.864864864864865],
        # [84293565.0,298977556.0,11108.0,30.0,20842.0,8006.0,792.0,579.0,63491.0,3092.0,0.0,0.0,1339.0,443.0,1646.0,3860982.0,176516.0,10985.0,4170.0,8104314.0,11656.0,30500.0,22591.0,273.0,93.0,320.0,333.0,2984.0,15526.0,5966.0,6838.0,13764.0,2918.0,6427.0,1268.0,4229.0,5101.0,3009.0,1,5.203083109919571,1.0311857436600411,2.6342925659472423,19.603535353535353,17.37878787878788,13.869949494949495],
        # [13377655.0,101491251.0,6739.0,0.0,22279.0,4245.0,366.0,200.0,0.0,4083.0,0.0,0.0,1069.0,295.0,489.0,1779015.0,146311.0,6700.0,1815.0,1798079.0,16640.0,20825.0,10109.0,459.0,46.0,270.0,589.0,1315.0,13227.0,5504.0,5604.0,17207.0,1379.0,8776.0,541.0,4509.0,8001.0,4079.0,1,10.058555133079848,2.9579405366207396,3.6914600550964187,36.13934426229508,47.013661202185794,18.306010928961747],
        # [26274744.0,135360623.0,700.0,0.0,1121.0,8.0,43.0,59.0,0.0,278.0,0.0,0.0,12.0,14.0,111.0,202564.0,18989.0,700.0,324.0,126064.0,1294.0,3476.0,1001.0,48.0,9.0,27.0,91.0,273.0,1067.0,575.0,579.0,2367.0,296.0,645.0,100.0,415.0,955.0,278.0,1,3.9084249084249083,0.9391891891891891,2.1604938271604937,24.813953488372093,55.04651162790697,16.27906976744186],
        # [65776440.0,88418176.0,1314.0,20.0,4491.0,4363.0,148.0,208.0,486.0,768.0,0.0,0.0,250.0,78.0,613.0,715984.0,33175.0,1283.0,915.0,874703.0,4486.0,4078.0,1907.0,138.0,33.0,61.0,160.0,821.0,2240.0,1542.0,1887.0,4190.0,816.0,2414.0,350.0,799.0,1983.0,699.0,1,2.728380024360536,0.8566176470588235,1.4021857923497267,15.135135135135135,28.31081081081081,8.66891891891892],
        # [18488910.0,158434360.0,2962.0,30.0,12795.0,19003.0,610.0,583.0,625.0,3680.0,0.0,0.0,438.0,1789.0,1712.0,2960527.0,193986.0,2946.0,3831.0,3583622.0,23184.0,79363.0,21975.0,586.0,96.0,213.0,647.0,3453.0,7400.0,7541.0,7671.0,20564.0,3632.0,12820.0,1226.0,2371.0,9173.0,3676.0,1,2.143064002316826,1.0121145374449338,0.7689898198903681,12.131147540983607,33.71147540983606,4.829508196721312],
        # [9147070.0,51881444.0,414.0,7.0,2116.0,508.0,89.0,92.0,25.0,416.0,0.0,0.0,46.0,170.0,279.0,433867.0,20527.0,414.0,652.0,666595.0,2944.0,10931.0,3751.0,93.0,19.0,33.0,147.0,570.0,1443.0,988.0,1095.0,4749.0,567.0,1618.0,224.0,518.0,2310.0,416.0,1,2.531578947368421,0.7336860670194003,0.6349693251533742,16.213483146067414,53.359550561797754,4.651685393258427],
        # [21053620.0,37404988.0,6308.0,14.0,21337.0,31318.0,748.0,469.0,425.0,7350.0,0.0,0.0,982.0,306.0,1382.0,3638001.0,286611.0,6289.0,7608.0,2129826.0,48689.0,15654.0,12082.0,1774.0,208.0,352.0,963.0,6974.0,13230.0,14124.0,15050.0,22035.0,6547.0,20821.0,2184.0,5255.0,11474.0,7337.0,1,1.897046171494121,1.1206659538720025,0.8266298633017876,17.68716577540107,29.45855614973262,8.407754010695188]
    # ]

    new_data = []
    for item in data:
        data_list = item[:38]+item[39:]
        new_data.append(data_list)
    # print(new_data)

    X_test_scaled = pd.DataFrame(new_data, columns=columns_)
    # scaler = StandardScaler()
    # X_test_scaled2 = scaler.fit_transform(X_test_scaled)

    y_pred = model.predict(X_test_scaled)

    return y_pred[0]

# print(judgment_cheater("Gokiton"))