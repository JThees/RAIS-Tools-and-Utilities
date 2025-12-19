import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import re

class TextCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Cleaner")
        self.root.geometry("600x450")
        
        # Configure style for dark theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Configure colors
        self.bg_color = "#2e2e2e"
        self.fg_color = "#ffffff"
        self.entry_bg = "#3e3e3e"
        self.button_bg = "#4a4a4a"
        self.highlight_bg = "#1e90ff"
        
        # Load phrases from file
        self.phrases_file = "phrases.txt"
        self.config_file = "config.txt"
        
        self.setup_ui()
        
        # Load phrases and config after UI is set up
        self.load_phrases_from_file()
        self.load_config()
        
    def setup_ui(self):
        # Configure root window
        self.root.configure(bg=self.bg_color)
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input file selection
        ttk.Label(main_frame, text="Source File:", foreground=self.fg_color, background=self.bg_color).pack(anchor='w')
        
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        self.input_path = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.input_path, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(input_frame, text="Browse...", command=self.browse_input).pack(side=tk.LEFT, padx=5)
        
        # Output options
        ttk.Label(main_frame, text="Output Options:", foreground=self.fg_color, background=self.bg_color).pack(anchor='w', pady=(10, 0))
        
        # Append to file option
        append_frame = ttk.Frame(main_frame)
        append_frame.pack(fill=tk.X, pady=5)
        
        self.append_var = tk.BooleanVar()
        ttk.Checkbutton(append_frame, text="Append to file:", variable=self.append_var, 
                       command=self.toggle_append, style='TCheckbutton').pack(side=tk.LEFT)
        
        self.append_path = tk.StringVar()
        self.append_entry = ttk.Entry(append_frame, textvariable=self.append_path, width=50, state='disabled')
        self.append_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        self.append_browse_btn = ttk.Button(append_frame, text="Browse...", command=self.browse_append, state='disabled', 
                  style='TButton')
        self.append_browse_btn.pack(side=tk.LEFT, padx=5)
        
        # Last n lines option
        last_lines_frame = ttk.Frame(main_frame)
        last_lines_frame.pack(fill=tk.X, pady=5)
        
        self.save_last_n = tk.BooleanVar()
        ttk.Checkbutton(last_lines_frame, text="Save last ", variable=self.save_last_n, 
                       command=self.toggle_last_n, style='TCheckbutton').pack(side=tk.LEFT)
        
        self.n_lines = tk.StringVar(value="10")
        self.n_entry = ttk.Spinbox(last_lines_frame, from_=1, to=1000, width=5, textvariable=self.n_lines, state='disabled')
        self.n_entry.pack(side=tk.LEFT, padx=(0, 5))
        # Bind to save config when value changes
        self.n_lines.trace('w', lambda *args: self.save_config())
        
        ttk.Label(last_lines_frame, text="lines to new file:", foreground=self.fg_color, 
                 background=self.bg_color).pack(side=tk.LEFT)
        
        self.new_file_path = tk.StringVar()
        self.new_file_entry = ttk.Entry(last_lines_frame, textvariable=self.new_file_path, width=40, state='disabled')
        self.new_file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.new_file_browse_btn = ttk.Button(last_lines_frame, text="Browse...", command=self.browse_new_file, state='disabled',
                  style='TButton')
        self.new_file_browse_btn.pack(side=tk.LEFT)
        
        # Overwrite option
        self.overwrite_var = tk.BooleanVar()
        self.overwrite_check = ttk.Checkbutton(main_frame, text="Overwrite existing file", variable=self.overwrite_var,
                       state='disabled', style='TCheckbutton')
        self.overwrite_check.pack(anchor='w', pady=(5, 0))
        
        # Phrases to strip option
        phrases_frame = ttk.Frame(main_frame)
        phrases_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(phrases_frame, text="Phrases to strip (loaded from phrases.txt):", 
                 foreground=self.fg_color, background=self.bg_color).pack(anchor='w')
        
        self.strip_phrases = tk.StringVar()
        self.strip_phrases_entry = ttk.Entry(phrases_frame, textvariable=self.strip_phrases, width=60)
        self.strip_phrases_entry.pack(fill=tk.X, pady=2)
        
        phrases_buttons = ttk.Frame(phrases_frame)
        phrases_buttons.pack(fill=tk.X, pady=2)
        
        ttk.Button(phrases_buttons, text="Save to phrases.txt", 
                  command=self.save_phrases_to_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(phrases_buttons, text="Reload from file", 
                  command=self.load_phrases_from_file).pack(side=tk.LEFT)
        
        ttk.Label(phrases_frame, text="Enter phrases separated by commas or use phrases.txt", 
                 foreground='#888888', background=self.bg_color, font=('Arial', 8)).pack(anchor='w')
        
        # Process button
        ttk.Button(main_frame, text="Process File", command=self.process_file, 
                  style='Accent.TButton').pack(pady=20)
        
        # Configure styles
        self.configure_styles()
    
    def configure_styles(self):
        self.style.configure('.', background=self.bg_color, foreground=self.fg_color)
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', background=self.bg_color, foreground=self.fg_color)
        self.style.configure('TButton', background=self.button_bg, foreground=self.fg_color)
        self.style.configure('TEntry', fieldbackground=self.entry_bg, foreground=self.fg_color)
        self.style.map('TButton',
                      background=[('active', self.highlight_bg)],
                      foreground=[('active', 'white')])
        self.style.map('TCheckbutton',
                     background=[('active', self.bg_color)],
                     foreground=[('active', self.fg_color)])
        self.style.configure('Accent.TButton', background=self.highlight_bg, foreground='white')
        
        # Configure disabled states
        self.style.map('TButton',
                      background=[('disabled', '#3a3a3a')],
                      foreground=[('disabled', '#6d6d6d')])
        
        # Configure spinbox
        self.style.configure('TSpinbox', fieldbackground=self.entry_bg, foreground=self.fg_color)
        
    def load_phrases_from_file(self):
        """Load phrases from phrases.txt file"""
        try:
            if os.path.exists(self.phrases_file):
                with open(self.phrases_file, 'r', encoding='utf-8') as f:
                    phrases = f.read().strip()
                    self.strip_phrases.set(phrases)
            else:
                # Create empty file if it doesn't exist
                with open(self.phrases_file, 'w', encoding='utf-8') as f:
                    f.write('')
                self.strip_phrases.set('')
        except Exception as e:
            print(f"Error loading phrases: {e}")
            self.strip_phrases.set('')
    
    def load_config(self):
        """Load configuration from config.txt file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith('last_n_lines='):
                            value = line.split('=')[1].strip()
                            if value.isdigit():
                                self.n_lines.set(value)
        except Exception as e:
            print(f"Error loading config: {e}")
    
    def save_config(self):
        """Save configuration to config.txt file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                f.write(f'last_n_lines={self.n_lines.get()}\n')
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def save_phrases_to_file(self):
        """Save current phrases to phrases.txt file"""
        try:
            phrases_text = self.strip_phrases.get().strip()
            with open(self.phrases_file, 'w', encoding='utf-8') as f:
                f.write(phrases_text)
            messagebox.showinfo("Success", "Phrases saved to phrases.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save phrases: {str(e)}")
        
    def browse_input(self):
        filetypes = [
            ('All Files', '*.*'),
            ('Text Files', '*.txt'),
            ('Markdown Files', '*.md')
        ]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.input_path.set(filename)
    
    def toggle_append(self):
        state = 'normal' if self.append_var.get() else 'disabled'
        self.append_entry.config(state=state)
        self.append_browse_btn.config(state=state)
    
    def toggle_last_n(self):
        state = 'normal' if self.save_last_n.get() else 'disabled'
        self.n_entry.config(state=state)
        self.new_file_entry.config(state=state)
        self.new_file_browse_btn.config(state=state)
        if state == 'normal':
            self.overwrite_check.config(state='normal')
        else:
            self.overwrite_check.config(state='disabled')
        # Save config when toggling
        self.save_config()
    
    def browse_append(self):
        filetypes = [
            ('All Files', '*.*'),
            ('Text Files', '*.txt'),
            ('Markdown Files', '*.md')
        ]
        filename = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=".txt")
        if filename:
            self.append_path.set(filename)
    
    def browse_new_file(self):
        filetypes = [
            ('All Files', '*.*'),
            ('Text Files', '*.txt'),
            ('Markdown Files', '*.md')
        ]
        filename = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=".txt")
        if filename:
            self.new_file_path.set(filename)
    
    def process_file(self):
        input_file = self.input_path.get()
        
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
            
        if not os.path.exists(input_file):
            messagebox.showerror("Error", f"File not found: {input_file}")
            return
        
        try:
            # Read the input file
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process the content (remove extra whitespace and specified phrases)
            # First strip phrases, then clean up whitespace
            strip_phrases_text = self.strip_phrases.get().strip()
            if strip_phrases_text:
                # Split by newlines first, then by commas
                phrases = []
                for line in strip_phrases_text.split('\n'):
                    line = line.strip()
                    if line:
                        # Split by comma if line contains commas
                        if ',' in line:
                            phrases.extend([p.strip() for p in line.split(',') if p.strip()])
                        else:
                            phrases.append(line)
                
                # Remove each phrase
                for phrase in phrases:
                    if phrase:
                        content = content.replace(phrase, '')
            
            # Now remove all whitespace (newlines, tabs, extra spaces)
            # More aggressive whitespace removal
            # Replace newlines and tabs with spaces first
            content = re.sub(r'[\n\r\t]+', ' ', content)
            # Remove multiple spaces
            content = re.sub(r' +', ' ', content)
            # Strip leading/trailing whitespace
            processed_content = content.strip()
            
            # Handle append to file
            if self.append_var.get():
                append_file = self.append_path.get()
                if not append_file:
                    messagebox.showerror("Error", "Please specify a file to append to.")
                    return
                
                with open(append_file, 'a', encoding='utf-8') as f:
                    f.write(processed_content + '\n')
                messagebox.showinfo("Success", f"Content appended to {append_file}")
            
            # Handle save last n lines to new file
            if self.save_last_n.get():
                new_file = self.new_file_path.get()
                if not new_file:
                    messagebox.showerror("Error", "Please specify an output file for the last n lines.")
                    return
                
                if os.path.exists(new_file) and not self.overwrite_var.get():
                    messagebox.showerror("Error", "Output file already exists. Enable 'Overwrite' to replace it.")
                    return
                
                try:
                    n = int(self.n_lines.get())
                    if n <= 0:
                        raise ValueError("Number of lines must be positive")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid number of lines.")
                    return
                
                # Get last n lines
                lines = content.splitlines()
                last_n_lines = lines[-n:] if len(lines) > n else lines
                
                with open(new_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(last_n_lines))
                
                messagebox.showinfo("Success", f"Last {n} lines saved to {new_file}")
            
            # If no output options were selected, show the processed content
            if not self.append_var.get() and not self.save_last_n.get():
                messagebox.showinfo("Processed Content", 
                                  "Here's the processed content (whitespace removed):\n\n" + 
                                  processed_content[:1000] + 
                                  ("..." if len(processed_content) > 1000 else ""))
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = TextCleanerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
