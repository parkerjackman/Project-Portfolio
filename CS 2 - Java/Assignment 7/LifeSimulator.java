

public class LifeSimulator {
    private int sizeX;
    private int sizeY;
    private boolean[][] grid;

    public LifeSimulator(int sizeX, int sizeY) {
        this.sizeX = sizeX;
        this.sizeY = sizeY;
        grid = new boolean[sizeX][sizeY];
    }

    public int getSizeX() {
        return sizeX;
    }

    public int getSizeY() {
        return sizeY;
    }

    public boolean getCell(int x, int y) {
        return grid[x][y];
    }

    public void insertPattern(Pattern pattern, int startX, int startY) {
        for (int x = 0; x < pattern.getSizeX(); x++) {
            for (int y = 0; y < pattern.getSizeY(); y++) {
                grid[startX + x][startY + y] = pattern.getCell(x, y);
            }
        }
    }

    public void update() {
        boolean[][] newGrid = new boolean[sizeX][sizeY];
        for (int x = 0; x < this.getSizeX(); x++) {
            for (int y = 0; y < this.getSizeY(); y++) {
                int neighbors = getNeighbors(x, y);

                if (neighbors == 3) {
                    newGrid[x][y] = true;
                }
                else if (grid[x][y] && neighbors ==2) {
                    newGrid[x][y] = true;
                }
            }
        }
        grid = newGrid;
    }

    public int getNeighbors(int x, int y) {
        int count = 0;
        for (int i = x - 1; i <= x + 1; i++) {
            for (int j = y - 1; j <= y + 1; j++) {
                if (i < 0) { continue; }
                if (j < 0) { continue; }
                if (i >= sizeX) { continue; }
                if (j >= sizeY) { continue; }
                if (i == x && j == y) { continue; }
                if (grid[i][j]) {
                    count++;
                }
            }
        }
        return count;
    }


}

