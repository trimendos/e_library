$(function() {

    $('#start').click(function() {
        $('#search').css("border", "");
        $('.errors').html('');
        var search = $('#search').val();
        $.ajax({
            url: '/searchResult',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                arr = jQuery.parseJSON(response);

                if('message' in arr){
                    $('.col-lg-12').html(arr['message']);
                    return;
                }
                if('errors' in arr){
                    var res = "",
                        tpl = "<li>[text]</li>";
                    for(var e in arr['errors']){
                        res += tpl.replace('[text]', arr['errors'][e])
                    }
                    $('.errors').html(res);
                    $('#search').css("border", "1px solid red");
                    return;
                }
                var res = "",
                    tpl_a = "<h4>Author: [name]</h4><p>Books: [books]</p>",
                    tpl_b = "<h4>Title: [title]</h4><p>Authors: [authors]</p>";

                if(arr['search_type'] == 'book'){
                    for(var book in arr.data){
                        res += tpl_b.replace('[title]', arr.data[book].title).
                               replace('[authors]', arr.data[book].authors.join(', '))
                    }
                    $('.col-lg-12').html(res);

                }else if(arr['search_type'] == 'author'){
                    for(var book in arr.data){
                        res += tpl_a.replace('[name]', arr.data[book].name).
                               replace('[books]', arr.data[book].books.join(', '))
                    }
                    $('.col-lg-12').html(res);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $(".search-param").click(function(){
        var val = $(this).text();
        $("button[class='btn dropdown-toggle'").text(val);
    });
});