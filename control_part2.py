from moviefiter import moviedata
import pandas as pd
user_1=moviedata()
def mainpart(user_ing, user_inc, user_date):
    

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

