// Program by Parker Jackman
import java.util.Scanner;

public class Quadratic {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Enter a, b, c: ");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

        double rootAmount = Math.pow(b, 2) - (4 * a * c);

        if (rootAmount > 0.0) {
            System.out.println("There are 2 roots for the quadratic equation with these roots.");
            double root1 = ((-b) + Math.sqrt(Math.pow(b,2) - (4 * a * c))) / (2 * a);
            double root2 = ((-b) - Math.sqrt(Math.pow(b,2) - (4 * a * c))) / (2 * a);
            System.out.println("r1 = " + root1);
            System.out.println("r2 = " + root2);
        }
        else if (rootAmount == 0.0) {
            System.out.println("There is 1 root for the quadratic equation with these roots.");
            double root1 = (-b) / (2 * a);
            System.out.println("r1 = " + root1);
        }
        else {
            System.out.println("There are no roots for the quadratic equation with these roots.");
        }
    }
}