function renderDate(data, type, full) {
    if (data.length == 0) {
        return "";
    }
    return moment(data, "DD/MM/YYYY").format("ll");
}

jQuery.extend(jQuery.fn.dataTableExt.oSort, {
    "price-pre": function(a) {
        if (a.length == 0) {
            return 0;
        }
        var x = a.split(" ")[0].substring(1);
        var ret = parseFloat(x);
        if (isNaN(ret)) {
            return 0;
        }
        return ret;
    },

    "price-asc": function(a, b) {
        return ((a < b) ? -1 : ((a > b) ? 1 : 0));
    },

    "price-desc": function(a, b) {
        return ((a < b) ? 1 : ((a > b) ? -1 : 0));
    }
});

$(document).ready(function() {
    $.fn.dataTable.moment('DD/MM/YYYY');

    $('#balls').DataTable({
        "paging": false,
        "bInfo": false,
        "bFilter": false,
        "aoColumnDefs": [{
            "aTargets": [1],
            "mData": "date",
            "mRender": renderDate
        }, {
            "bSortable": false,
            "aTargets": ["no-sort"]
        },{
            "sType": "price",
            "aTargets": [4]
        }],
        "order": [
            [1, "asc"]
        ],
    });
});

// Track outbound link events
function _gaLt(event) {
    var el = event.srcElement || event.target;

    /* Loop up the DOM tree through parent elements if clicked element is not a link (eg: an image inside a link) */
    while (el && (typeof el.tagName == 'undefined' || el.tagName.toLowerCase() != 'a' || !el.href)) {
        el = el.parentNode;
    }

    if (el && el.href) {
        /* link */
        var link = el.href;
        if (link.indexOf(location.host) == -1 && !link.match(/^javascript\:/i)) { /* external link */
            /* HitCallback function to either open link in either same or new window */
            var hitBack = function(link, target) {
                target ? window.open(link, target) : window.location.href = link;
            };
            /* Is target set and not _(self|parent|top)? */
            var target = (el.target && !el.target.match(/^_(self|parent|top)$/i)) ? el.target : false;
            /* send event with callback */
            ga(
                "send", "event", "Outgoing Links", link,
                document.location.pathname + document.location.search, {
                    "hitCallback": hitBack(link, target)
                }
            );

            /* Prevent standard click */
            event.preventDefault ? event.preventDefault() : event.returnValue = !1;
        }

    }
}

/* Attach the event to all clicks in the document after page has loaded */
var w = window;
w.addEventListener ? w.addEventListener("load", function() {
    document.body.addEventListener("click", _gaLt, !1)
}, !1) : w.attachEvent && w.attachEvent("onload", function() {
    document.body.attachEvent("onclick", _gaLt)
});
