class DataUnit:
    def __init__(self):
        self.__result_dict = []

    def add_data(self, data):
        self.__result_dict.append(data)

    def get_final_values(self):
        return self.__result_dict


""",First Name,Last Name,SSN,Address,Company,Department,Position,Zip,Mobile number
0,Kraig,Pollich,450-70-0086,"972 Joycelyn Causeway, Roobfurt, NC 28368","Gorczany, Hartmann and Lind",IT,dental hygienist,71531-1363,737.591.9348
1,Manual,Hermiston,100-79-3942,"2960 Reiko Road, Shanahanhaven, ME 77044",Lubowitz-Reichert,IT,astronomer,21603,999.024.7276
2,Lala,Greenfelder,018-84-1052,"Apt. 876 612 Tromp Forge, Shennafurt, AL 35408-8332","Walsh, Cole and Hahn",IT,carpenter,84030,(552) 622-0475
3,Claudette,Hermann,237-36-3480,"Suite 576 27978 Angla Mission, Hudsonside, MD 11455",Koss-Reynolds,IT,firefighter,43495-2392,(786) 048-7302
4,Olinda,Dooley,193-43-2685,"Apt. 205 28009 Roberts Ford, Arnoldfort, WA 91159","Corkery, Lakin and Klocko",IT,carpenter,51094,760.609.8182
5,Chere,McDermott,107-56-7325,"Apt. 467 471 Schultz Fields, New Kyle, SC 32107",Okuneva-Moen,IT,electrician,80297,874-426-1148"""
