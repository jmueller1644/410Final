var imgURL = chrome.extension.getURL("icons/green_circle.png");
var urls = Array();
$("li.g").each(function(){
      if ($(this).find("cite").text().indexOf(".") != -1 && $(this).find(".intrlu") != undefined && !$(this).hasClass("no-sep")) {
        url = $(this).find(".r a").eq(0).attr("href");
        urls.push(url);
        $(this).find(".r").eq(0).parent().html("<table><tr><td>" + $(this).find(".r").eq(0).parent().html() + "</td><td>" + '<img src="' + imgURL +'" alt="green"></td></tr></table>');
      }
  });

$.post("http://localhost:8888/urls", {sites: JSON.stringify(urls)}, function(data) {
    console.log(data);
  });