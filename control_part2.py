from moviefiter import moviedata
import pandas as pd
user_1=moviedata()
def mainpart(user_ing, user_inc, user_date):
    
    try:
        genresls=user_ing.lstrip().rstrip().split(",")
        castls=user_inc.lstrip().rstrip().split(",")
        datels=int(user_date.lstrip().rstrip()[0:4])
        wanted_df=moviedata.search(user_1.movies_df,Only=False,genres=genresls,cast=castls)
        secondpart=moviedata.search(user_1.movies_df,Only=False,genres=genresls)
        final_one=pd.concat([wanted_df,secondpart],axis=0)
        final_one.drop_duplicates(subset=['id'],keep='first',inplace=True)
        moviedata.forsort(wanted_df,datels)
        if wanted_df.shape[0]>100:
            return wanted_df.head(100)
        else:
            return wanted_df
    except:
        return 'Error'


def df_tolist(df:pd.DataFrame):
    final_output=[]
    empty_list = []
    print(f"From df_list: {df}")
    for row in range(df.shape[0]):
        id_ofmovie=df["id"].iloc[row] #HERE to put id eg.862 all in str
        output=user_1.alles_inner_extract(df=user_1.movies_df,movie_ids=[id_ofmovie],usemydf=True,rEALLYONLY=True) #using id of the movie to extract data
        final_output.append(output)
        return final_output
    
    
    #add extraction of movie title from list
        
    #OUTPUT FORMAT:
    #!!! if shown nan means this movie does not has this section.Just skip   
    #get every row by final_output[row]
    #get each elements in each row by following: 
    #final_output[row][position]
    #data type: str
    #position: 0:movie_id for input upon  
    #position: 1 title of movie
    #position: 2 overview, can be add to shown on the page  
    #position: 3 tagline, a line of words can be also add to page
    #position: 4 a list of main actors.
    #position: 5 a list of genres of this movie
    #position: 6 a list of maker of this movie
    #position: 7 a list of the of country of this movie  format: "XX_[Country]"
    #position: 8 the year it released

# from moviefiter import moviedata
# import pandas as pd
# import threading as td
# import datetime

# user_1=moviedata()
# def mainpart(user_ing, user_inc, user_date):
#  def mainpart():
   
#     #user_ing=input("genres:")  #input by terminal
#     user_ing="animation,horror,funny,lol" #input genres
#     # for multiple genres use "," to seperate each keywords.
#     #user_inc=input("casts: ") #by terminal
#     user_inc="tom hanks"       #input actors
#     #user_date=input("date: ")
#     user_date="2011"           #input datetime
#     if len(user_ing.lstrip().rstrip())>0:
#         genresls=user_ing.lstrip().rstrip().split(",")
#     else:
#         genresls=[]
#     #print(genresls)
#     if len(user_inc.lstrip().rstrip())>0:
#         castls=user_inc.lstrip().rstrip().split(",")
#     else:
#         castls=[]
#     #print(castls)
#     if len(user_date.lstrip().rstrip())>=4:
#         datels=user_date.lstrip().rstrip()[0:4]
#     else:
#         datels=str(datetime.datetime.today().year)
#     #print(datels)
#     #newp_global_ones=[]
#     No_cast=False
#     No_genre=False

#     if len(genresls)>0:
#         args_gc={"genres":genresls}
#         td_gc=td.Thread(
#             target=user_1.search,
#             args=(user_1.movies_df,),kwargs={"Only":False,**args_gc} #simply nope 
#             )
#         #print("UYESE UITW ORKDS")
        
#         td_gc.start()
#         if len(castls)>0:
#             wanted_df=user_1.search(user_1.movies_df,Only=False,upload=False,genres=genresls,cast=castls)
#         else:
#             wanted_df=pd.DataFrame()
#             No_cast=True
#         td_gc.join()
#     else:
#         No_genre=True

#     secondpart=user_1.newp_global_ones
#     #print(secondpart)
#     if No_cast and No_genre:
#         final_one=user_1.movies_df.head(10)
#     else:
        
#         final_one=pd.concat([wanted_df,secondpart],axis=0)

#     final_one.drop_duplicates(subset=['id'],keep='first',inplace=True)
#     final_one=moviedata.forsort(final_one,datels)


#     if final_one.shape[0]>10:
#         return final_one.head(10)
#     else:
#         return final_one


# def df_tolist(df:pd.DataFrame):
#     final_output=[]
#     empty_list = []
#     print(f"From df_list: {df}")
#     for row in range(df.shape[0]):
#         id_ofmovie=df["id"].iloc[row] #HERE to put id eg.862 all in str
#         output=user_1.alles_inner_extract(df=user_1.movies_df,movie_ids=[id_ofmovie],usemydf=True,rEALLYONLY=True) #using id of the movie to extract data
#         final_output.append(output)
#         return final_output
    
    
#     #add extraction of movie title from list
        
#     #OUTPUT FORMAT:
#     #!!! if shown nan means this movie does not has this section.Just skip   
#     #get every row by final_output[row]
#     #get each elements in each row by following: 
#     #final_output[row][position]
#     #data type: str
#     #position: 0:movie_id for input upon  
#     #position: 1 title of movie
#     #position: 2 overview, can be add to shown on the page  
#     #position: 3 tagline, a line of words can be also add to page
#     #position: 4 a list of main actors.
#     #position: 5 a list of genres of this movie
#     #position: 6 a list of maker of this movie
#     #position: 7 a list of the of country of this movie  format: "XX_[Country]"
#     #position: 8 the year it released



