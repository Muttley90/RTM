function buildUrl(){
  var data = $("#selectedDate").datepicker('getDate');
  var serv = $("#selectedServ").find(":selected").text();
  var x = serv+"/"+data;
  console.log(x)
  return x;
}
