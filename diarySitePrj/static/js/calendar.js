var Calendar = function(divId) {

    //Store div id
    this.divId = divId;

    // Days of week, starting on Sunday
    this.DaysOfWeek = [
        '일',
        '월',
        '화',
        '수',
        '목',
        '금',
        '토'
    ];

    // Months, stating on January
    this.Months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월' ];

    // Set the current month, year
    var d = new Date();
    this.CurrentMonth = d.getMonth();
    this.CurrentYear = d.getFullYear();

};

// Goes to next month
Calendar.prototype.nextMonth = function() {
    if ( this.CurrentMonth == 11 ) {
        this.CurrentMonth = 0;
        this.CurrentYear = this.CurrentYear + 1;
    }
    else {
        this.CurrentMonth = this.CurrentMonth + 1;
    }
    this.showCurrent();
};

// Goes to previous month
Calendar.prototype.previousMonth = function() {
    if ( this.CurrentMonth == 0 ) {
        this.CurrentMonth = 11;
        this.CurrentYear = this.CurrentYear - 1;
    }
    else {
        this.CurrentMonth = this.CurrentMonth - 1;
    }
    this.showCurrent();
};

// Show current month
Calendar.prototype.showCurrent = function() {
    this.showMonth(this.CurrentYear, this.CurrentMonth);
};

// Show month (year, month)
Calendar.prototype.showMonth = function(y, m) {

    var d = new Date()
        // First day of the week in the selected month
        , firstDayOfMonth = new Date(y, m, 1).getDay()
        // Last day of the selected month
        , lastDateOfMonth =  new Date(y, m+1, 0).getDate()
        // Last day of the previous month
        , lastDayOfLastMonth = m == 0 ? new Date(y-1, 11, 0).getDate() : new Date(y, m, 0).getDate();

    var html = '<table class="table">';

    // Write selected month and year
    html += '<tr><td colspan="7">' + this.Months[m] + ' - ' + y + '</td></tr>';

    // Write the header of the days of the week
    html += '<tr>';
    for(var i=0; i < this.DaysOfWeek.length;i++) {
        html += '<td>' + this.DaysOfWeek[i] + '</td>';
    }
    html += '</tr>';

    // Write the days
    var i=1;
    var format_m;
    var format_d;
    var temp_m;
    do {

        var row = new Date(y, m, i).getDay();

        // If Sunday, start new row
        if (row == 0) {
            html += '<tr>';
        }
        // If not Sunday but first day of the month
        // it will write the last days from the previous month
        else if (i == 1) {
            html += '<tr>';
            var k = lastDayOfLastMonth - firstDayOfMonth + 1;
            for (var j = 0; j < firstDayOfMonth; j++) {
                html += '<td class="not-current">' + k + '</td>';
                k++;
            }
        }


        // Write the current day in the loop
        temp_m = m + 1
        if (temp_m < 10)
            format_m = "0" + temp_m;
        else
            format_m = temp_m

        if (i < 10)
            format_d = "0" + i;
        else
            format_d = i

        html += '<td>' + '<a href=' + y + '/' + format_m + '/' + format_d + '>' + i + '</a>' + '</td>';

        // If Saturday, closes the row
        if (row == 6) {
            html += '</tr>';
        }
        // If not Saturday, but last day of the selected month
        // it will write the next few days from the next month
        else if (i == lastDateOfMonth) {
            var k = 1;
            for (row; row < 6; row++) {
                html += '<td class="not-current">' + k + '</td>';
                k++;
            }
        }

        i++;
    } while (i <= lastDateOfMonth);

    // Closes table
    html += '</table>';

    // Write HTML to the div
    document.getElementById(this.divId).innerHTML = html;
};

// On Load of the window
window.onload = function() {

    // Start calendar
    var c = new Calendar("divCalendar");
    c.showCurrent();

    // Bind next and previous button clicks
    getId('btnNext').onclick = function() {
        c.nextMonth();
    };
    getId('btnPrev').onclick = function() {
        c.previousMonth();
    };
}

// Get element by id
function getId(id) {
    return document.getElementById(id);
		}
