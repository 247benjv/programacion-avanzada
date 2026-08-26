package org.example;
import java.math.BigInteger;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static BigInteger linearFactorial(int n){
        BigInteger result = BigInteger.ONE;
        for (int i = 2; i <= n; i++){
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }

    public static BigInteger recursiveFactorial(int n){
        if (n == 0 || n == 1) {
            return BigInteger.ONE;
        }
        return BigInteger.valueOf(n).multiply(recursiveFactorial(n-1));
    }

    public static void main(String[] args) {

        int[] nvalues = {10, 50, 100, 250, 500, 1000, 2000, 5000};

        System.out.println("n\tTiempo lineal (ns) \tTiempo recursivo(ns)");

        //para medir el tiempo de la version lineal
        for (int n : nvalues) {
            long linearStart = System.nanoTime();
            linearFactorial(n);
            long linearFinish = System.nanoTime();
            long linearTime = linearFinish - linearStart;

            //para medir el tiempo de la version recursiva
            long recursiveStart = System.nanoTime();
            recursiveFactorial(n);
            long recursiveFinish = System.nanoTime();
            long recursiveTime = recursiveFinish - recursiveStart;

            System.out.println(n + "\t" + linearTime + "\t\t" + recursiveTime);
        }
    }
}