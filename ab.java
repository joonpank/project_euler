package abc;
import java.util.*;
import java.lang.Math;

public class ab {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		long number = 600851475143L;
		List<Long> list = new ArrayList<Long>();
		long i = 2;
		
		// To check primes we take sqrt(number) as an upper limit
		while (i < (long) Math.ceil(Math.sqrt(number))) {

			if (number % i == 0) {
				
				boolean add_list = true;
				
				// set up upper limit when checking if prime already is in it.
				long upper_limit = (long) Math.ceil(Math.sqrt(i));
				
					for (long j = 1; j < upper_limit; j++) {
				
						if (i % j == 0) {
							
							if (list.contains(j) == true) {
								add_list = false;
								break;
							}
						}
					}
				
				if (add_list == true) {
					System.out.println("Added new prime to a list " + i);
					list.add(i);
				}
			}
			
			i++;
		}
		System.out.println(list);
		
			
	}

}
