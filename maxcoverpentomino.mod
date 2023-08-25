int row = 6;
int column = 10;
int f = 50;
int p = 12;
int P[1..p][1..f][1..row][1..column] = ...;


dvar boolean x[1..p][1..f];
dvar boolean y[1..row][1..column];
dvar int result[1..row][1..column];



maximize sum(r in 1..row, c in 1..column)y[r][c];

subject to {
  forall(r in 1..row, c in 1..column) sum(p in 1..p, f in 1..f) (P[p][f][r][c] * x[p][f]) <= 1;
  
  forall(r in 1..row, c in 1..column) sum(p in 1..p, f in 1..f) (P[p][f][r][c] * x[p][f]) == y[r][c];
  
  forall(r in 1..row, c in 1..column) sum(p in 1..p, f in 1..f) (P[p][f][r][c] * x[p][f]*p) == result[r][c];
  
  
  forall(p in 1..p) sum(f in 1..f) x[p][f] <= 1;
}


