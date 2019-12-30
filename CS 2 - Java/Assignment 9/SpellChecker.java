import java.io.*;
import java.util.ArrayList;
import java.util.Dictionary;
import java.util.Scanner;

public class SpellChecker {
    public static void main(String[] args) {

        // Step 1: Demonstrate tree capabilities
        testTree();

        // Step 2: Read the dictionary and report the tree statistics
        BinarySearchTree<String> dictionary = readDictionary();
        reportTreeStats(dictionary);

        // Step 3: Perform spell checking
        spellCheck("letter.txt", dictionary);

    }

    //Displays an error message, program exits
    public static void quitError(String msg)
    {
        System.out.println(msg);
        System.out.println("Program will now quit.");
        System.exit(0);
    }



    /**
     * This method is used to help develop the BST, also for the grader to
     * evaluate if the BST is performing correctly.
     */
    public static void testTree() {
        BinarySearchTree<String> tree = new BinarySearchTree<>();

        //
        // Add a bunch of values to the tree
        tree.insert("Olga");
        tree.insert("Tomeka");
        tree.insert("Benjamin");
        tree.insert("Ulysses");
        tree.insert("Tanesha");
        tree.insert("Judie");
        tree.insert("Tisa");
        tree.insert("Santiago");
        tree.insert("Chia");
        tree.insert("Arden");

        //
        // Make sure it displays in sorted order
        tree.display("--- Initial Tree State ---");
        reportTreeStats(tree);

        //
        // Try to add a duplicate
        if (tree.insert("Tomeka")) {
            System.out.println("oops, shouldn't have returned true from the insert");
        }
        tree.display("--- After Adding Duplicate ---");
        reportTreeStats(tree);

        //
        // Remove some existing values from the tree
        tree.remove("Olga");    // Root node
        tree.remove("Arden");   // a leaf node
        tree.display("--- Removing Existing Values ---");
        reportTreeStats(tree);

        //
        // Remove a value that was never in the tree, hope it doesn't crash!
        tree.remove("Karl");
        tree.display("--- Removing A Non-Existent Value ---");
        reportTreeStats(tree);
    }

    /**
     * This method is used to report on some stats about the BST
     */
    public static void reportTreeStats(BinarySearchTree<String> tree) {
        System.out.println("-- Tree Stats --");
        System.out.printf("Total Nodes : %d\n", tree.numberNodes());
        System.out.printf("Leaf Nodes  : %d\n", tree.numberLeafNodes());
        System.out.printf("Tree Height : %d\n", tree.height());
    }

    /**
     * This method reads the dictionary and constructs the BST to be
     * used for the spell checking.
     */
    public static BinarySearchTree<String> readDictionary() {
        BinarySearchTree<String> tree = new BinarySearchTree<>();

        ArrayList<String> words = new ArrayList<String>();

        try {
            BufferedReader br = new BufferedReader(new FileReader("Dictionary.txt"));
            while (br.ready()) {
                words.add(br.readLine());
            }
        }

        catch(FileNotFoundException filenotfoundexception) //Catches file not found exception
        {
            System.out.println("File not found.");
        }
        catch (java.io.IOException IOException)
        {
            System.out.println("IO Exception");
        }

        java.util.Collections.shuffle(words, new java.util.Random(System.currentTimeMillis()));

        for (int i = 0; i < words.size(); i++) {
            tree.insert(words.get(i));
        }

        return tree;
    }

    public static void spellCheck(String checkMe, BinarySearchTree<String> dictionary) {
        System.out.println("--- Misspelled Words in File ---");
        try {
            Scanner s = new Scanner(new FileReader(checkMe));
            String currentWord = s.next().toLowerCase();
            while (s.hasNext()) {
                if (!dictionary.search(currentWord.replaceAll("[,:.!?()]",""))) {
                    System.out.println(currentWord.replaceAll("[,:.!?()]",""));
                }
                currentWord = s.next().toLowerCase();
            }

        } catch(FileNotFoundException filenotfoundexception) //Catches file not found exception
        {
            System.out.println("File not found.");
        }

    }

}
