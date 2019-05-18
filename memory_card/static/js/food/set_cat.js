;

var foodcat_set_ops ={
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        $(".wrap_cat_set .save").click(
            function () {

                var btn_target = $(this);
                if (btn_target.hasClass("disabled")) {

                    common_ops.alert("正是处理！！请不要重复提交")
                    return
                }
                var catname_target = $(".wrap_cat_set input[name = name]");
                var catname =catname_target.val();

                var weight_target = $(".wrap_cat_set input[name = weight]");
                var weight =weight_target.val();








                


                var data ={
                    name:catname,
                    weight:weight,

                    id:$(".wrap_cat_set input[name = id]").val()

                };
                btn_target.addClass("disabled");
                $.ajax({
                    url:common_ops.buildUrl("/card/cat-set"),
                    type:"POST",
                    data:data,
                    dataType:'json',
                    success:function (res) {
                        btn_target.removeClass("disabled");

                        var callback = null;

                        if (res.code== 200){
                            callback =function () {
                                window.location.href =  common_ops.buildUrl("/card/cat")
                                
                            }

                        }
                        common_ops.alert( res.msg,callback);

                        
                    }
                })

            }

        )
        
    }
    
    
};

$(document).ready(
    function () {
       foodcat_set_ops.init();
    }
)