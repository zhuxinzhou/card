;

var card_set_fun = {

    init: function () {
        this.ue = null;
        this.eventBind();
        this.initEditor();
    },

    eventBind: function () {
        var that = this;

        $(".wrap_card_set .upload_pic_wrap input[name=pic]").change(function () {
            $(".wrap_card_set .upload_pic_wrap").submit();
        });

        $(".wrap_card_set select[name=cat_id]").select2({
            language: "zh-CN",
            width: '100%'
        });

        $(".wrap_card_set input[name=tags]").tagsInput({
            width: 'auto',
            height: 40,
            onAddTag: function (tag) {
            },
            onRemoveTag: function (tag) {
            }
        });

        // 修改
        $(".wrap_card_set .change").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理，请稍后。");
                return;
            }

            // 获取数据
            //
            // 分类 无数据库
            let formid_location = $(".wrap_card_set select[name=fromid]");
            let fromid = formid_location.val();
            // 卡片名称
            let card_name_location = $(".wrap_card_set input[name=card_name]");
            let card_name = card_name_location.val();
            // 复习状态
            let study_status_location = $(".wrap_card_set select[name=study_status]");
            let study_status = study_status_location.val();
            // 状态 0 未归档 1 已归档
            let status_location = $(".wrap_card_set select[name=status]");
            let status = status_location.val();
            // 卡片内容
            let card_content_location = $(".wrap_card_set input[name=card_content]");
            let card_content = $.trim(that.ue.getContent());
            // 下一次复习时间
            let last_time_date_location = $("#date");
            let last_time_hour_location = $("#hour");
            let last_time_minute_location = $("#minute");
            let last_time_date = last_time_date_location.val();
            let last_time_hour = last_time_hour_location.val();
            let last_time_minute = last_time_minute_location.val();

            // 前端验证
            if (parseInt(fromid) < 0) {
                common_ops.tip("请选择分类！", formid_location);
                return;
            }

            if (card_name.length < 1) {
                common_ops.tip("请输入卡片名称！", card_name_location);
                return;
            }

            if (card_content.length < 10) {
                common_ops.tip("请输入描述，不能少于10个字符", card_content_location);
                return;
            }

            if (Number(status) !== 0 && Number(status) !== 1) {
                common_ops.tip("请选择正确数据！", status_location);
                return;
            }

            if (!time_judge(last_time_date, last_time_hour, last_time_minute)) {
                common_ops.tip("请输入正确的时间", last_time_date_location);
                return;
            }

            btn_target.addClass("disabled");

            var put_data = {
                card_name: card_name,
                card_content: card_content,
                study_status: study_status,
                status: status,
                last_time: last_time_date + ' ' + last_time_hour + ':' + last_time_minute + ':00'
            };

            $.ajax({
                url: common_ops.buildUrl("/card"),
                type: 'PUT',
                data: put_data,
                dataType: 'json',
                success: function (result) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (result.code === 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/card/index");
                        }
                    }
                    common_ops.alert(result.msg, callback);
                }
            });

        });

        // 添加
        $(".wrap_card_set .save").click(function () {

            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理，请稍后。");
                return;
            }

            // 获取数据
            //
            // 分类 无数据库
            let formid_location = $(".wrap_card_set select[name=fromid]");
            let fromid = formid_location.val();
            // 卡片名称
            let card_name_location = $(".wrap_card_set input[name=card_name]");
            let card_name = card_name_location.val();
            // 卡片内容 富文本
            let card_content_location = $(".wrap_card_set input[name=card_content]");
            let card_content = $.trim(that.ue.getContent());

            // 下一次复习时间
            let last_time_date_location = $("#date");
            let last_time_hour_location = $("#hour");
            let last_time_minute_location = $("#minute");
            let last_time_date = last_time_date_location.val();
            let last_time_hour = last_time_hour_location.val();
            let last_time_minute = last_time_minute_location.val();

            // 前端验证
            if (parseInt(fromid) < 0) {
                common_ops.tip("请选择分类！", formid_location);
                return;
            }

            if (card_name.length < 1) {
                common_ops.tip("请输入卡片名称！", card_name_location);
                return;
            }

            if (card_content.length < 10) {
                common_ops.tip("请输入描述，不能少于10个字符", card_content_location);
                return;
            }

            if (!time_judge(last_time_date, last_time_hour, last_time_minute)) {
                common_ops.tip("请输入正确的时间", last_time_date_location);
                return;
            }

            btn_target.addClass("disabled");

            var data = {
                card_name: card_name,
                card_content: card_content,
                last_time: last_time_date + ' ' + last_time_hour + ':' + last_time_minute + ':00'
            };

            // 修改 / 添加
            $.ajax({
                url: common_ops.buildUrl("/card"),
                type: 'POST',
                data: data,
                dataType: 'json',
                success: function (result) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (result.code === 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/card/index");
                        }
                    }
                    common_ops.alert(result.msg, callback);
                }
            });
        });
    },

    initEditor: function () {
        var that = this;
        that.ue = UE.getEditor('editor', {
            toolbars: [
                ['undo', 'redo', '|',
                    'bold', 'italic', 'underline', 'strikethrough', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', '|', 'rowspacingtop', 'rowspacingbottom', 'lineheight'],
                ['customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
                    'directionalityltr', 'directionalityrtl', 'indent', '|',
                    'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
                    'link', 'unlink'],
                ['imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
                    'insertimage', 'insertvideo', '|',
                    'horizontal', 'spechars', '|', 'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols']

            ],
            enableAutoSave: true,
            saveInterval: 60000,
            elementPathEnabled: false,
            zIndex: 4,
            serverUrl: common_ops.buildUrl('/upload/ueditor')
        });
    },
};

$(document).ready(function () {
    card_set_fun.init();
});

function time_judge(date_info, hour, minute) {
    let now_time = new Date();
    let time_str = date_info.replace("/-/g", "/");
    let get_time = new Date(time_str);

    if (get_time < now_time) {
        return false;
    } else {
        if (now_time.getHours() < hour) {
            return false;
        } else {
            if (now_time.getMinutes() < minute) {
                return false;
            }
        }
    }
    return true;
}