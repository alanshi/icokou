//获取地理位置
function getLocation()
{
    if (navigator.geolocation)
        {
            navigator.geolocation.getCurrentPosition(getPosition,showError);
        }
    else
        {
            //x.innerHTML="浏览器不支持获取您当前地理位置信息.";
        }
}
//获取经纬度
function getPosition(position)
{
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;    
    var latlon = position.coords.latitude+","+position.coords.longitude;
    return latlon;
}
//错误处理
function showError(error)
{
  switch(error.code) 
    {
    case error.PERMISSION_DENIED:
      //x.innerHTML="User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      //x.innerHTML="Location information is unavailable."
      break;
    case error.TIMEOUT:
      //x.innerHTML="The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      //x.innerHTML="An unknown error occurred."
      break;
    }
}