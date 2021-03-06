;
var card_index_fun = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;

        // 删除 / 归档
        $(".remove").click(function () {
            that.removeCard($(this).attr("data"))
        });

        // 搜索
        $(".wrap_search .search").click( function(){
                $(".wrap_search").submit();
        });
    },
    removeCard: function (id) {
        var callback = {
            'ok': function () {
                $.ajax({
                    url: common_ops.buildUrl("/card/" + id),
                    type: 'DELETE',
                    dataType: 'json',
                    success: function (result) {
                        let callback = null;
                        if (result.code === 200) {
                            callback = function () {
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert(result.msg, callback);
                    }
                });
            },
            'cancel': null
        };
        common_ops.confirm("确定删除？", callback);
    }
};

$(document).ready(function () {
    card_index_fun.init();
});