import datetime
from lunardate import LunarDate
class Date():
  def __init__(self):
    self.today=datetime.date.today()#获取今天的日期信息
    weekday = self.today.weekday()
    self.weekday_names = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    self.today_weekday=self.weekday_names[weekday]
    New_year=datetime.date(self.today.year, 1, 1)#元旦
    Lunar_Spring=LunarDate(self.today.year,1,1)
    Labor_day=datetime.date(self.today.year, 5, 1)#劳动节
    Lunar_Tomb= datetime.date(self.today.year, 4, 5)
    Lunar_Dragon = LunarDate(self.today.year,5,5)
    Lunar_Autumn=LunarDate(self.today.year,8,15)
    National_Day=datetime.date(self.today.year, 10, 1)#国庆节
    # 使用lunardate库进行日期转换
    self.Festival_list=[('元旦',New_year,'solar'),('春节',Lunar_Spring,'Lunar'),('劳动节',Labor_day,'solar'),('清明节',Lunar_Tomb,'solar'),
                        ('端午节',Lunar_Dragon,'Lunar'),('中秋节',Lunar_Autumn,'Lunar'),('国庆节',National_Day,'solar')]
    try:
      with open("data.txt","r",encoding='UTF-8') as f:
        diy_hdays=f.readlines()
      for diy_hday in diy_hdays:
        if diy_hday=='':
          break
        diy_hday=diy_hday.strip()
        list_diy=diy_hday.split("&")
        if list_diy[2]=='solar':
          date_obj=self.str_to_date(list_diy[1])
        else:
          date_obj=self.str_to_date(list_diy[1],True)
        tuple1=(list_diy[0],date_obj,list_diy[2])
        self.Festival_list.append(tuple1)
    except:
      pass
    self.list_date_dif=[]#用于储存各个节日距离今天的有多少天
    #储存节日名和节日日期对象
    for tuple1 in self.Festival_list:
      if tuple1[2]=='solar':#如果日期是按阳历存的
        if self.today<tuple1[1]:#如果还没过
          date_dif=(tuple1[1]-self.today).days#计算差几天
          tuple_National=(tuple1[0],date_dif)#连同节日名一起储存
          self.list_date_dif.append(tuple_National)#存入列表
        else:#如果当年次节日已过
          next_year_date=datetime.date(self.today.year+1,tuple1[1].month,tuple1[1].day)#计算明年该节日日期
          date_dif=(next_year_date-self.today).days
          tuple_National=(tuple1[0],date_dif)
          self.list_date_dif.append(tuple_National)
      else:#如果是按阴历存的
        if self.today<=tuple1[1].toSolarDate():
          solar_date=tuple1[1].toSolarDate()#阴历转化成阳历
          date_dif=(solar_date-self.today).days
          tuple_National=(tuple1[0],date_dif)
          self.list_date_dif.append(tuple_National)
        else:#如果当年次节日已过
          next_solar_date=LunarDate(self.today.year+1,tuple1[1].month,tuple1[1].day).toSolarDate()
          date_dif=(next_solar_date-self.today).days
          tuple_National=(tuple1[0],date_dif)
          self.list_date_dif.append(tuple_National)
    self.list_date_dif.sort(key=lambda element:element[1])#从小到大排列
  def str_to_date(self,date,lunar=False):
    date_list=date.split('/')
    if len(date_list)==3:#输入带年份
      try:
          year, month,day = map(int,date_list)
          if 0< year <100:
            year+=2000
          if lunar:
            date=LunarDate(year,month,day).toSolarDate()#如果是阴历转换成阳历
          else:
            date=datetime.date(year,month,day)
      except ValueError:
          return None
    elif len(date_list)==2:
      try:
          month,day = map(int,date_list)
          if lunar:
            date=LunarDate(self.today.year,month,day).toSolarDate()#如果是阴历转换成阳历
          else:
            date=datetime.date(self.today.year,month,day)
      except ValueError:
          return None    
    else:
      return None
    return date
  def cal_dif(self,from_,to_,flunar=False,tlunar=False):#2023/11/2
    if isinstance(from_, str):
      from_=self.str_to_date(from_,flunar)
    if isinstance(to_, str):
      to_=self.str_to_date(to_,tlunar)
    if (from_==None) or (to_==None):
      return None
    date_dif=(to_-from_).days
    return date_dif
  def today_interval(self,date,lunar=False):
    if isinstance(date, str):
      date=self.str_to_date(date=date,lunar=lunar)
    if date==None:
      return None
    date_dif=(self.today-date).days
    if date_dif<0:
      date_dif=-date_dif
    return date_dif
  def myweekday(self,date,lunar=False):
    if isinstance(date, str):
      date=self.str_to_date(date=date,lunar=lunar)
    if date==None:
      return None
    return self.weekday_names[date.weekday()]
  def data_save(self,name,date,lunar=False):
    date_list=date.split('/')   
    if len(date_list)==2:
      try:
          month,day = map(int,date_list)
          if lunar:
            date1=LunarDate(self.today.year,month,day).toSolarDate()#如果是阴历转换成阳历
          else:
            date1=datetime.date(self.today.year,month,day)
      except ValueError:
          return False    
    else:
      return False
    try:
      with open("data.txt","a",encoding='UTF-8') as f:
        if lunar:
          f.write(name+'&'+date+'&lunar\n')
        else:
          f.write(name+'&'+date+'&solar\n')
      return True
    except:
      return False
if __name__=='__main__':
  a=Date()
  b=a.cal_dif('3243',"134314")
  print(b)