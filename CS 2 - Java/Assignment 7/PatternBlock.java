
public class PatternBlock extends Pattern {
    private int sizeX = 2;
    private int sizeY = 2;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return patternBlock[x][y];
    }

    private boolean[][] patternBlock = {
            {true, true},
            {true, true}
    };
}