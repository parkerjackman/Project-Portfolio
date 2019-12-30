
public class PatternBlinker extends Pattern {
    private int sizeX = 1;
    private int sizeY = 3;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return patternBlinker[x][y];
    }

    private boolean[][] patternBlinker = {
            {true, true, true}

    };
}