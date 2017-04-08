push_1  { 	}
push_-16  {		    }
store		 push_2  { 	 }
push_44  { 	 		  }
store		 push_3  { 		}
push_32  { 	     }
store		 push_4  { 	  }
push_0  {	 }
store		 push_5  { 	 	}
push_1  { 	}
store		 label
  { }
start_loop_push_5  { 	 	}
push_4  { 	  }
retrieve			push_4  { 	  }
duplicate 
 push_5  { 	 	}
retrieve			duplicate 
 print_as_number	
 	push_2  { 	 }
retrieve			print_as_char	
  push_3  { 		}
retrieve			print_as_char	
  store		 retrieve			add	   store		 push_1  { 	}
duplicate 
 duplicate 
 duplicate 
 retrieve			add	   store		 retrieve			jump_if_negative
		{ }
push_10  { 	 	 }
push_46  { 	 			 }
duplicate 
 duplicate 
 print_as_char	
  print_as_char	
  print_as_char	
  print_as_char	
  quit


end
