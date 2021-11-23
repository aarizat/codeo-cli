using System;
using System.Collections.Generic;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            HashSet<int> letters = new HashSet<int>();
            bool isDuplicate = false;
            var input = Console.ReadLine();
            
            foreach (var character in input) {
                if (letters.Contains((int)character)) {
                    isDuplicate = true; 
                    break;
                }
                else
                    letters.Add((int)character); 
            }

            if (!isDuplicate)
                Console.WriteLine("no");
            else
                Console.WriteLine("yes");

        }
    }
}