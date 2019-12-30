

public class JulianDate extends Date {


    JulianDate() {
        // sets date as current date
        super(1, 1, 1);
        addDays(719164);

        long timeSinceDate = System.currentTimeMillis();
        timeSinceDate += java.util.TimeZone.getDefault().getRawOffset();

        int daysToAdd = (int) (timeSinceDate / 86400000);
        addDays(daysToAdd);
    }

    JulianDate(int year, int month, int day) {
        // sets date as specified in parameters
        super(year, month, day);
    }

    @Override
    public boolean isLeapYear() {

        return (super.getCurrentYear() % 4) == 0;
    }





}
