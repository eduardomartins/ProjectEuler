/*
 * sem título.c
 * 
 * Copyright 2014 Eduardo Sant Anna Martins <eduardo@eduardo-notebook>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <stdlib.h>
#include <stdio.h>

unsigned long long int fibonacci(unsigned long long int n){
	if(n == 0){
		return 0;
	}
	else if(n == 1){
		return 1;
	}
	else{
		return fibonacci(n-1) + fibonacci(n-2);
	}

}

unsigned long long int fatoral(unsigned long long int n){
	if(n == 0) {
		return 1;
	}
	else{
		return n * fatoral(n-1);
	}
}

unsigned long long int pascal(unsigned long long int n, unsigned long long int p){
	if(n >= p){
		return fatoral(n)/( fatoral(p) * fatoral(n - p) );
	}
	else{
		return 0; 
	}
}

unsigned long long int fibonacci_pascal(unsigned long long int n, unsigned long long int k = 1){
	printf("HERE(n = %llu, k = %llu)\n", n, k);
	if(n == 0){
		return 0;
	}
	if ( ((n % 2 == 1) && (n - k) == (k - 1)) || ((n % 2 == 0) && ((n - k) - (k - 1)) == 1) ){
		return pascal(n - k, k - 1);
	}
	else{
		return pascal(n - k, k - 1) + fibonacci_pascal(n, k + 1);
	}
}
unsigned long long int quantidade(char *s){
	if(s[0] == '\0'){
		return 0;
	}
	else{
		return 1  + quantidade(&s[1]);
	}
}

int digito(char c){
	return (c >= '0' && c <= '9') ? c - 48 : -1;
}

int numero(char *s, unsigned long int k = 1){
	int n, c;
	if(s[0] == '\0'){
		return 0;
	}
	else{
		n = quantidade(s) - 1;
		c = digito(s[n]);
		s[n] = '\0';
		return k * c + numero(s, 10 * k);
	}
}


int main(int argc, char **argv)
{	
	unsigned long long int n;
	if(argc < 2){
		printf("Modo de uso: %s <token> \n", argv[0]);
	}
	else{
		n = numero(argv[1]);
		printf("%llu\n", fibonacci_pascal(n)); 	
	}
	return 0;
}

