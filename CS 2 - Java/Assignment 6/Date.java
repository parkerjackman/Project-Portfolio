

public class Date {
    private int day;
    private int month;
    private int year;


    Date(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public void addDays(int days) {
        // add days to instance date
        for (int i = 1; i <= days; i++) {
            this.day = day + 1;
            if (this.day > getNumberOfDaysInMonth(this.year, this.month)) {
                this.month += 1;
                this.day = 1;
            }
            if (this.month > 12) {
                this.year += 1;
                this.month = 1;
            }
        }
    }

    public void subtractDays(int days) {
        // subtract days from instance date
        for (int i = 1; i <= days; i++) {
            this.day = day - 1;
            if (this.day <= 0) {
                this.month -= 1;
                this.day = getNumberOfDaysInMonth(this.year, this.month);
            }
            if (this.month <= 0) {
                this.year -= 1;
                this.month = 12;
                this.day = 31;
            }
        }
    }

    public boolean isLeapYear() {
        return true;
    }

    public void printShortDate() {
        // print date using int for month
        System.out.print(month + "/" + day + "/" + year);
    }

    public void printLongDate() {
        // print date using String for month
        System.out.print(getMonthName(month) + " " + day + ", " + year);
    }

    public String getCurrentMonthName() {
        return getMonthName(month);
    }

    public int getCurrentMonth() { return month; }

    public int getCurrentYear() { return year; }

    public int getCurrentDayOfMonth() { return day; }

    private int getNumberOfDaysInMonth(int year, int month) {
        switch (month) {
            case 1:
                return 31;
            case 2:
                if (isLeapYear()) {
                    return 29;
                }
                else {
                    return 28;
                }
            case 3:
                return 31;
            case 4:
                return 30;
            case 5:
                return 31;
            case 6:
                return 30;
            case 7:
                return 31;
            case 8:
                return 31;
            case 9:
                return 30;
            case 10:
                return 31;
            case 11:
                return 30;
            case 12:
                return 31;
            default:
                return 0;
        }
    }

    private int getNumberOfDaysInYear(int year) {
        if (isLeapYear()) {
            return 366;
        } else {
            return 365;
        }
    }

    private String getMonthName(int month) {

        switch(month) {
            case 1:
                return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return "September";
            case 10:
                return "October";
            case 11:
                return "November";
            case 12:
                return "December";
            default:
                return "null";
        }
    }




}

