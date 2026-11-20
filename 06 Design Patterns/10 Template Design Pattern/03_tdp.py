from abc import ABC, abstractmethod
from typing import final

class ModelTrainer(ABC):
        
    @abstractmethod
    def load_data(self):
        pass
    
    @abstractmethod
    def preprocess_data(self):
        pass
    
    @abstractmethod
    def train_model(self):
        pass
    
    @abstractmethod
    def evaluate_model(self):
        pass
    
    @abstractmethod
    def save_model(self):
        pass
    
    @final
    def templateMethod(self):
        self.load_data()
        self.preprocess_data()
        self.train_model()
        self.evaluate_model()
        self.save_model()
        
class RandomForest(ModelTrainer):
    def load_data(self):
        print('Load data for Random Forest')
        
    def preprocess_data(self):
        print('Preprocess data for Random Forest')
        
    def train_model(self):
        print('Training Model for Random Forest')
        
    def evaluate_model(self):
        print('Evaluating Model for Random Forest')
        
    def save_model(self):
        print('Saving Model for Random Forest')


class SVM(ModelTrainer):
    def load_data(self):
        print('Load data for SVM')
        
    def preprocess_data(self):
        print('Preprocess data for SVM')
        
    def train_model(self):
        print('Training Model for SVM')
        
    def evaluate_model(self):
        print('Evaluating Model for SVM')
        
    def save_model(self):
        print('Saving Model for SVM')
    
    def templateMethod(self):
        self.load_data()
        self.preprocess_data()
        self.train_model()
        self.evaluate_model()
        print('---------------')
        self.save_model()

random_forest = RandomForest()
random_forest.templateMethod()

svm = SVM()
svm.templateMethod()

# final keywrod is useful in compile time - When code is in vscode any good type checking extension can flag issues
# But in runtime (when code is executed) - final keyword dosent play any significant role and if template method is overridden then it will be executed

# There are chances that Loading, saving etc could be same across all the types of Algorithms (Random Forest, SVM, Newural Network)
# In that case those methods will also be defined in ModelTrainer class along with templateMethod function
# And if needed those methods can be overridden but not templateMethod function