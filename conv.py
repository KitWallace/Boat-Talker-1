points = ["N","NNE","NE","ENE","E","ESE","SE" ,"SSE" ,"S", "SSW","SW","WSW","W", "WNW","NW","NNW","N"]
point_text = ["North","Nor Nor East","North East","East North East","East","Eeast Sow East","Sow East" ,"Sow Sow East" ,"South", "Sow Sow West","Sow West","West Sow West","West", "West Nor West","Nor West","Nor Nor West","North"]

def deg_to_dms(dd,latlong) :

   if (latlong == "lat"):
      if (dd< 0) :
         dir = "West"
      else :
         dir = "East"
   else :
      if (dd< 0) :
         dir = "South"
      else :
         dir = "North"

   dd = abs(dd)
   deg = int(dd)
   min = (dd - deg ) * 60
   dmin = int(min)
   sec = int((min - dmin) * 60)
   return "".join([str(deg)," degrees ", str(dmin), "minutes ",str(sec) , " seconds ", dir])

def degree_to_compass_point(deg) :
   dp = deg + 11.25
   dp = dp % 360 
   dp = int(dp // 22.5)
   return points[dp]

def degree_to_compass_point_text(deg) :
   dp = deg + 11.25
   dp = dp % 360 
   dp = int(dp // 22.5)
   return point_text[dp]





