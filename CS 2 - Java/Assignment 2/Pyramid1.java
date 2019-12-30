import java.util.Scanner;

public class Pyramid1 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of lines: ");
        int numLines = input.nextInt();

        int numDigits = countDigits(numLines);
        int minWidth = numDigits + 1;
        String standardFormat = "%" + minWidth + "d";
        int firstWidth = (numLines * minWidth) + minWidth;

        for (int currentNum = 1; currentNum <= numLines; currentNum++){
            firstWidth -= minWidth;
            String pivotFormat = "%n%" + firstWidth + "d";
            System.out.printf(pivotFormat, currentNum);

            for (int countDown = currentNum - 1; countDown >= 1; countDown--){
                System.out.printf(standardFormat, countDown);
            }

            for (int countUp = 2; countUp <= currentNum; countUp++){
                System.out.printf(standardFormat, countUp);
            }
        }
    }

    public static int countDigits(int value){
        int numDigits = 0;
        while (value > 0){
            value = value / 10;
            numDigits++;
        } return numDigits;
    }
}