

public class JulianDate {

    private int year;
    private int month;
    private String monthLong;
    private int day;
    private boolean isLeapYear;

    JulianDate() {
        // sets date as current date
        year = 1;
        month = 1;
        day = 1;
        addDays(719164);

        long timeSinceDate = System.currentTimeMillis();
        timeSinceDate += java.util.TimeZone.getDefault().getRawOffset();

        int daysToAdd = (int)(timeSinceDate / 86400000);
        addDays(daysToAdd);
    }

    JulianDate(int year, int month, int day) {
        // sets date as specified in parameters
        this.year = year;
        this.month = month;
        this.day = day;
        this.monthLong = getMonthName(month);
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
                this.month = month - 1;
                this.day = getNumberOfDaysInMonth(this.year, this.month);
            }
            if (this.month <= 0) {
                this.year = year - 1;
                this.month = 12;
                this.day = 31;
            }
        }
    }

    public boolean isLeapYear() {
        // is the specified year a leap year?
        isLeapYear = isLeapYear(year);
        return isLeapYear;
    }

    public void printShortDate() {
        // print date using int for month
        System.out.print(month + "/" + day + "/" + year);
    }

    public void printLongDate() {
        // print date using String for month
        monthLong = getMonthName(month);
        System.out.print(monthLong + " " + day + ", " + year);
    }

    public String getMonthName() {
        monthLong = getMonthName(month);
        return monthLong;
    }

    public int getMonth() { return month; }

    public int getYear() { return year; }

    public int getDayOfMonth() { return day; }

    private boolean isLeapYear(int year) {

        isLeapYear = (year % 4) == 0;
        return isLeapYear;
    }

    private int getNumberOfDaysInMonth(int year, int month) {
        int numberOfDays = 0;
        switch (month) {
            case 1:
                numberOfDays = 31;
                break;
            case 2:
                if (isLeapYear(year)) {
                    numberOfDays = 29;
                }
                else {
                    numberOfDays = 28;
                }
                break;
            case 3:
                numberOfDays = 31;
                break;
            case 4:
                numberOfDays = 30;
                break;
            case 5:
                numberOfDays = 31;
                break;
            case 6:
                numberOfDays = 30;
                break;
            case 7:
                numberOfDays = 31;
                break;
            case 8:
                numberOfDays = 31;
                break;
            case 9:
                numberOfDays = 30;
                break;
            case 10:
                numberOfDays = 31;
                break;
            case 11:
                numberOfDays = 30;
                break;
            case 12:
                numberOfDays = 31;
                break;

        }
        return numberOfDays;
    }

    private int getNumberOfDaysInYear(int year) {
        int numberOfDays = 365;
        if (isLeapYear(year)) {
            numberOfDays = 366;
        }
        return numberOfDays;
    }

    private String getMonthName(int month) {

        switch(month) {
            case 1:
                monthLong = "January";
                break;
            case 2:
                monthLong = "February";
                break;
            case 3:
                monthLong = "March";
                break;
            case 4:
                monthLong = "April";
                break;
            case 5:
                monthLong = "May";
                break;
            case 6:
                monthLong = "June";
                break;
            case 7:
                monthLong = "July";
                break;
            case 8:
                monthLong = "August";
                break;
            case 9:
                monthLong = "September";
                break;
            case 10:
                monthLong = "October";
                break;
            case 11:
                monthLong = "November";
                break;
            case 12:
                monthLong = "December";
        }
        return monthLong;
    }

}