using System; // Tímto říkáme, že budeme používat základní systémové příkazy

class Program
{
    static void Main()
    {
        // 1. POŽÁDÁME O VSTUP
        // Console.Write vypíše text, ale neukončí řádek (kurzor zůstane za textem)
        Console.Write("Zadejte počet vajec: ");
        
        // Console.ReadLine() přečte text, ale my ho musíme převést na číslo (int)
        int vejce = int.Parse(Console.ReadLine());

        // 2. DEFINUJEME PROMĚNNÉ
        // V C# musíme vždy říct typ (int = celé číslo) a ukončit řádek středníkem ;
        int velikostPlata = 6;
        int pocetPlat = vejce / velikostPlata; // Pozor: u int v C# funguje "/" jako celočíselné dělení!
        int zbytek = vejce % velikostPlata;

        // 3. VÝPIS VÝSLEDKU
        
        Console.WriteLine($"Máš celkem {vejce} vajec.");
        Console.WriteLine($"Naplníš {pocetPlat} plat a zbyde ti {zbytek} vajec.");
        
        // Tento řádek tam dáváme, aby se okno programu hned nezavřelo (čeká na stisk klávesy)
        Console.WriteLine("Stiskni libovolnou klávesu pro ukončení...");
        Console.ReadKey();
    }
}
