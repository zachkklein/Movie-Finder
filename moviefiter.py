import pandas as pd
import numpy as np
import io
import ast
import warnings

warnings.filterwarnings("ignore")
class moviedata():
    
    def __init__(self) -> None:
        self.credits_2_df=pd.read_csv("archive/credits.csv").drop_duplicates().copy()
        self.movies_df=pd.read_csv("archive/movies_metadata.csv",dtype=str).filter(items=["adult","popularity","budget","genres","homepage","id","imdb_id","original_title","overview","production_companies","production_countries","release_date","spoken_languages","vote_average","vote_count","tagline"]).copy()
        #user 
        # first use search to find their like movies:output movie id (yep)
        # then find the wanted genre,wanted 
        #def search by cast
        #def search by date
        #def search by genre
        

        # if user class
        #wanted: 喜欢的工作室集，喜欢的电影国家集，喜欢的人物出现集，喜欢的分类集\
        #只做简易板，先收集喜欢集，然后在这些集里面选，选了加genre分，如果不喜欢减两分，然后search最高分的几个，先把最高分弄出来，然后后面的依次按照popularity排列出来。
        #时间先求mean值，然后选择这个时间段的进行推荐，越靠近这个时间的先放出来。
        #国家集同理genre。
        #喜欢的人物同理genre，作为genre加分项，如果有喜欢的人出演，genre
        #筛选优先度，genere，（公司，国家，人物），时间，流行度
        #genre中
        #加权：百分之25，
        #先进行样本框选，然后
        # only useful remained
        #then merge the credit df with movie df
        #similarities in 
        # date mean
        # popularity high low
        # vote high to low
        # sim: production companies, genre(specific genre), date(get a range of time), production countries(low priority), people(extract the people in liked movie)
        self.movies_df=pd.concat([self.movies_df,self.credits_2_df],axis=1,join="outer")
        inx=self.movies_df.shape[1]-1
        self.movies_df=self.movies_df.iloc[:,[x for x in range(inx)]]
        self.movies_df=self.movies_df.dropna(axis=0,how="any",subset=["adult","popularity","budget","genres","homepage","id","imdb_id","original_title","overview","production_companies","production_countries","release_date","spoken_languages","vote_average","vote_count"])
        self.userdata=[]



    def forsort(df,givendate):
        df.insert(0,"date_diff",[int(-abs(int(givendate)-int(df["release_date"].iloc[x][0:4]))) for x in range(df.shape[0])])
        #self.movies_df.sort_values(by=["date_diff"],ascending=False,inplace=True)
        df.sort_values(by=["date_diff","vote_average","popularity"],ascending=False,inplace=True)

        return df

    #multi search
    @staticmethod
    def search(dfs,Only=True,inputByUSER=True,**args): # Only means if it is false show all starts with values given true means show the ones totally equal to value.
        isNum=True
        if inputByUSER:
            for eachkeys in args:
                    if eachkeys=="production_countries":
                        for eachele in range(len(args[eachkeys])):
                            newpword=""
                            for eachword in args[eachkeys][eachele]:
                                newpword+=eachword.upper()
                        
                            
                            args[eachkeys][eachele]=newpword.lstrip().rstrip()
                    
                    else:
                        for eachele in range(len(args[eachkeys])):
                            newpword=""
                            for eachword in args[eachkeys][eachele]:
                                newpword+=eachword.lower()
                                if(eachword.isalpha()):
                                    isNum=False
                            newpword.lstrip().rstrip()
                            if isNum:
                                continue
                            else:
                                tempstrlist=newpword.lstrip().rstrip().split(" ")
                                temp=" ".join("".join(x[0].upper()+x[1:]) for x in tempstrlist)
                                args[eachkeys][eachele]=temp
            #print (type(args),args)
            return moviedata.__search_implement(df=dfs,Only=Only,kwargs=args)
        else:
            return moviedata.__search_implement(df=dfs,Only=Only,kwargs=args)
    
    @staticmethod
    def __search_implement(df:pd.DataFrame,Only:bool,kwargs:dict):  #a:[1,2,3,4,56]
        newp=df.copy()   # i is column, j is row 
        if not Only:
            for i in kwargs:
                def func(x:pd.DataFrame):
                    count = False
                    if i=="genres":
                        temp_ones=moviedata.innerframe_extract(x["genres"].iloc[0],["name"]) 
                        for rows in range(temp_ones.shape[0]):
                            
                            for j in range(len(kwargs[i])):
                                
                                if(str(temp_ones["name"].iloc[rows]).find(str(kwargs[i][j]))!=-1):
                                    count=True
                                    break
                    
                    elif i=="cast":
                        temp_ones=moviedata.innerframe_extract(x["cast"].iloc[0],["name"])
                        temp_ones=temp_ones.head(3)
                        #print(temp_ones)
                        #temp_ones=temp_ones.iloc[:,[0]] #only popular ones first half remained
                        for rows in range(temp_ones.shape[0]):
                           
                            for j in range(len(kwargs[i])):
                                
                                if(str(kwargs[i][j]).find(str(temp_ones["name"].iloc[rows]))!=-1):
                                    count=True
                                    break
               
                    elif i=="production_companies":
                        temp_ones=moviedata.innerframe_extract(x["production_companies"].iloc[0],["name"])
                        for rows in range(temp_ones.shape[0]):
                         
                            for j in range(len(kwargs[i])):
                                
                                if(str(temp_ones["name"].iloc[rows]).find(str(kwargs[i][j]))!=-1):
                                    count=True
                                    break
                
                    elif i=="production_countries": #input is US,CH,RU,likwise
                        temp_ones=moviedata.innerframe_extract(x["production_countries"].iloc[0],["iso_3166_1"])
                        for rows in range(temp_ones.shape[0]):
                    
                            for j in range(len(kwargs[i])):
                                if(str(temp_ones["iso_3166_1"].iloc[rows]))[0:3]==(str(kwargs[i][j])[0:3]):
                                    count=True
                                    break
      
                    else:    
                        for j in range(len(kwargs[i])):
                            if(str(x[i].iloc[0]).startswith(str(kwargs[i][j]))):
                                count=True
                                break
                    return count
                            
                newp=newp.groupby(i).filter(func)
        else:
            for i in kwargs:
                def func(x:pd.DataFrame):
                    count = False
                    if i=="genres":
                        temp_ones=moviedata.innerframe_extract(x["genres"].iloc[0],["name"]) 
                        for rows in range(temp_ones.shape[0]):
                     
                            for j in range(len(kwargs[i])):
                                
                                if(str(temp_ones["name"].iloc[rows])==(str(kwargs[i][j]))):
                                    count=True
                                    break

                    elif i=="cast":
                        temp_ones=moviedata.innerframe_extract(x["cast"].iloc[0],["name"])
                        temp_ones=temp_ones.head(3)
                        #print(temp_ones)
                        #temp_ones=temp_ones.iloc[:,[0]]#only popular ones first half remained
                        for rows in range(temp_ones.shape[0]):
                    
                            for j in range(len(kwargs[i])):
                                    
                                if(str(kwargs[i][j])).startswith(str(temp_ones["name"].iloc[rows])):
                                    count=True
                                    break
                
                    elif i=="production_companies":
                        temp_ones=moviedata.innerframe_extract(x["production_companies"].iloc[0],["name"])
                        for rows in range(temp_ones.shape[0]):
                            
                            for j in range(len(kwargs[i])):
                                    
                                if(str(temp_ones["name"].iloc[rows])==(str(kwargs[i][j]))):
                                    count=True
                                    break        
                    elif i=="production_countries": #input is US,CH,RU,likwise
                        temp_ones=moviedata.innerframe_extract(x["production_countries"].iloc[0],["iso_3166_1"])
                        for rows in range(temp_ones.shape[0]):
                          
                              for j in range(len(kwargs[i])):
                                if(str(kwargs[i][j])[0:3]==(str(temp_ones["iso_3166_1"].iloc[rows]))[0:3]):
                                    count=True
                                    break
                   
                    else:  
                        for j in range(len(kwargs[i])):
                            if(str(x[i].iloc[0])==(str(kwargs[i][j]))):
                                count=True
                                break
                    return count
                            
                newp=newp.groupby(i).filter(func)
        return newp


        """ rubbish:)()
       for i in kwargs:
            try:
                def cut_all(groupdf):
                    groupdf.insert(groupdf.shape[1],"tempcopy",groupdf[i])
                    for j in range(groupdf.shape[0]):
                        groupdf[i].iloc[j]=groupdf[i].iloc[j][0:len(kwargs[i])]
                        #print(len(groupdf[i].iloc[j][0:len(kwargs[i])])) 
                    return groupdf
                
                def to_origin(groupdf):
                    groupdf[i]=groupdf["tempcopy"]
                    groupdf=groupdf.iloc[:,[x for x in range(groupdf.shape[1]-1)]]
                    return groupdf
                #newpgroup=newp.groupby(i)
                newp=newp.groupby(i).apply(cut_all)  
                newp=newp.groupby(i).get_group(kwargs[i])
                newp=newp.groupby(i).apply(to_origin)
            except KeyError:
                print("Not Found")
        """
        
    
    @staticmethod
    def innerframe_extract(df_postion_staff:str,filterlist=[]):
        temp_list=ast.literal_eval(df_postion_staff)
        if(len(filterlist)>0):
            return pd.DataFrame(temp_list,dtype=str).filter(filterlist)
        else:
            return pd.DataFrame(temp_list,dtype=str)
        



    def add_userdata(self,movie_idsl:list): #dont use it, it simply for multi users
        self.userdata.append(self.add_userdata(movie_ids=movie_idsl))
    
    def alles_inner_extract(self,movie_ids:list,rEALLYONLY=True,df=pd.DataFrame(),usemydf=False): # serach the cast 找出用户喜欢的电影中出现的角色 ,genre
            #print(self.movies_df["id"].iloc[_0]) #REALLYONLY SAME as only 
            #this part idont wanna write method and iter it because it seems many bugs will flow out and difficult to read in iter state
        if usemydf:
            wantedmovies_df=moviedata.search(df,Only=rEALLYONLY,id=movie_ids)
        else:
            wantedmovies_df=moviedata.search(self.movies_df,Only=rEALLYONLY,id=movie_ids) # find the user wanted movies, ONLY SHOULD BE TRUE
        #castline_newp=pd.DataFrame({"name&gender":[],"count":[]},dtype=str)
        #genreline_newp=pd.DataFrame({"id&name":[],"count":[]},dtype=str)
        #companyline_newp=pd.DataFrame({"companyname":[],"count":[]},dtype=str)
        #country_newp=pd.DataFrame({"countryname":[],"count":[]},dtype=str)
        
        #timeline_newp=np.array(wantedmovies_df["release_date"].apply(lambda x:int(x[0:4])),dtype=float)
        #timeline_newp=int(round(float(timeline_newp.mean(keepdims=True)),0))
        castline_newp=[]
        genreline_newp=[]
        companyline_newp=[]
        country_newp=[]
        #empty data init
        #print(wantedmovies_df)
        for _0 in range(wantedmovies_df.shape[0]):
            try:
                credits_cast=moviedata.innerframe_extract(wantedmovies_df["cast"].iloc[_0],["name","gender"])
                temp_moviekew=moviedata.innerframe_extract(wantedmovies_df["genres"].iloc[_0],["name"]) 
                temp_company=moviedata.innerframe_extract(wantedmovies_df["production_companies"].iloc[_0],["name"])
                temp_country=moviedata.innerframe_extract(wantedmovies_df["production_countries"].iloc[_0])
        
                #extract parts

                #credits_cast=credits_cast.groupby("gender").filter(lambda x: int(x["gender"].iloc[0])>0) #kill zero ones
                credits_cast=credits_cast.iloc[[0,1,2],:] #only popular ones first half remained

                for _1 in range(temp_country.shape[0]): #iso_3166_1   name   combine iso and name together
                    temp_country["iso_3166_1"].iloc[_1]=temp_country["iso_3166_1"].iloc[_1].lstrip().rstrip()+"_["+temp_country["name"].iloc[_1].lstrip().rstrip()+"]"
                temp_country=temp_country.iloc[:,[0]] 
                #wash parts
            except: #all excepts show that this position is empty
                continue
            else:#build parts
                #castline_newp=pd.concat([castline_newp,credits_cast],axis=0)
                #genreline_newp=pd.concat([genreline_newp,temp_moviekew],axis=0)
                for _2 in range(credits_cast.shape[0]):#join name and gender together Yes oR add up the count number CREDIT part
                    nginfo="_".join([str(credits_cast["name"].iloc[_2]),str(credits_cast["gender"].iloc[_2])]) 
                    castline_newp.append(nginfo)
                        
                        

                for _2 in range(temp_moviekew.shape[0]):#join name and gender together Yes oR add up the count number GENRE part
                    ninfo=str(temp_moviekew["name"].iloc[_2])
                    genreline_newp.append(ninfo)

                

                for _2 in range(temp_company.shape[0]):#join name and gender together Yes oR add up the count number COMPANY part
                    com_info=str(temp_company["name"].iloc[_2])
                    companyline_newp.append(com_info)

                for _2 in range(temp_country.shape[0]):#join name and gender together Yes oR add up the count number COMPANY part
                    area_info=str(temp_country["iso_3166_1"].iloc[_2])
                    country_newp.append(area_info)
                        


        return [wantedmovies_df["id"].iloc[_0],wantedmovies_df["original_title"].iloc[_0],wantedmovies_df["overview"].iloc[_0],wantedmovies_df["tagline"].iloc[_0],castline_newp,genreline_newp,companyline_newp,country_newp,wantedmovies_df["release_date"].iloc[_0][0:4]]

                         
        
