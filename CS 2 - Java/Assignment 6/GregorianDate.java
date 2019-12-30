

public class GregorianDate extends Date {


    GregorianDate() {
        // sets date as current date ???
        super(1970, 1, 1);

        long timeSinceDate = System.currentTimeMillis();
        timeSinceDate += java.util.TimeZone.getDefault().getRawOffset();

        int daysToAdd = (int) (timeSinceDate / 86400000);
        addDays(daysToAdd);
    }

    GregorianDate(int year, int month, int day) {
        // sets date as date specified in parameters
        super(year, month, day);
    }

    @Override
    public boolean isLeapYear() {

        boolean divisibleBy4 = (super.getCurrentYear() % 4) == 0;
        boolean divisibleBy100 = (super.getCurrentYear() % 100) == 0;
        boolean divisibleBy400 = (super.getCurrentYear() % 400) == 0;

        if (!divisibleBy4) {
            return false;
        } else if (!divisibleBy100) {
            return true;
        } else if (!divisibleBy400) {
            return false;
        } else {
            return true;
        }
    }


}